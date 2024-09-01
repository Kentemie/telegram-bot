import asyncio

from typing import Optional

from aiogoogle import Aiogoogle

from async_property import async_cached_property

from src.core.services.google.base import GoogleServiceManager
from src.core.services.google.drive import GoogleDriveManager


class GoogleSheetsManager(GoogleServiceManager):
    def __init__(
        self,
        service_account_key_path: str,
        scopes: list[str],
        drive_manager: GoogleDriveManager,
    ):
        super().__init__(service_account_key_path, scopes)

        self.aiogoogle = Aiogoogle(service_account_creds=self.creds)
        self.drive_manager = drive_manager

        self._spreadsheets: Optional[list[tuple[str, str]]] = None  # [(id, name),]
        self._spreadsheets_lock = asyncio.Lock()

        self._spreadsheet_tables: dict[str, list[str]] = (
            {}
        )  # spreadsheet_id: [table_name]
        self._spreadsheet_tables_lock = asyncio.Lock()

    @async_cached_property
    async def _sheets_api(self):
        return await self.aiogoogle.discover("sheets", "v4")

    async def _get_spreadsheets(self) -> None:
        async with self._spreadsheets_lock:
            self._spreadsheets = await self.drive_manager.get_files(
                q="mimeType='application/vnd.google-apps.spreadsheet'"
            )

    async def get_spreadsheets(self) -> list[tuple[str, str]]:
        if self._spreadsheets is None:
            await self._get_spreadsheets()

        return self._spreadsheets

    async def _get_spreadsheet_tables(self, spreadsheet_id: str):
        async with self._spreadsheet_tables_lock:
            async with self.aiogoogle as aiogoogle:
                response = await aiogoogle.as_service_account(
                    (await self._sheets_api).spreadsheets.get(
                        spreadsheetId=spreadsheet_id,
                    )
                )

            self._spreadsheet_tables[spreadsheet_id] = [
                sheet["properties"]["title"] for sheet in response.get("sheets")  # noqa
            ]

    async def get_spreadsheet_tables(self, spreadsheet_idx: str) -> list[str]:
        spreadsheet_id = self._spreadsheets[int(spreadsheet_idx)][0]

        if spreadsheet_id not in self._spreadsheet_tables:
            await self._get_spreadsheet_tables(spreadsheet_id)

        return self._spreadsheet_tables[spreadsheet_id]

    async def get_data(
        self,
        spreadsheet_idx: str,
        table_name: str,
        column_start: str,
        column_end: str,
        row_start: str = "",
        row_end: str = "",
    ) -> Optional[list[list[list[str]]]]:
        spreadsheet_id = self._spreadsheets[int(spreadsheet_idx)][0]

        ranges = [
            f"{table_name}!A:A",
            f"{table_name}!{column_start}{row_start}:{column_end}{row_end}",
        ]

        async with self.aiogoogle as aiogoogle:
            response = await aiogoogle.as_service_account(
                (await self._sheets_api).spreadsheets.values.batchGet(
                    spreadsheetId=spreadsheet_id,
                    ranges=ranges,
                )
            )

        return [r.get("values", []) for r in response.get("valueRanges")]  # noqa
