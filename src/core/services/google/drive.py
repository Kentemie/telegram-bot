from typing import Any

from aiogoogle import Aiogoogle

from async_property import async_cached_property

from src.core.services.google.base import GoogleServiceManager


class GoogleDriveManager(GoogleServiceManager):
    def __init__(self, service_account_key_path: str, scopes: list[str]):
        super().__init__(service_account_key_path, scopes)

        self.aiogoogle = Aiogoogle(service_account_creds=self.creds)

    @async_cached_property
    async def _drive_api(self):
        return await self.aiogoogle.discover("drive", "v3")

    async def get_files(
        self, q: str, fields: str = "files(id, name)"
    ) -> list[tuple[str, str]]:
        async with self.aiogoogle as aiogoogle:
            response = await aiogoogle.as_service_account(
                (await self._drive_api).files.list(
                    q=q,
                    fields=fields,
                )
            )

        return [
            (file["id"], file["name"]) for file in response.get("files", [])  # noqa
        ]
