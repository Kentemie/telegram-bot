from aiogram.types import CallbackQuery, BufferedInputFile

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select

from src.core.services.google import google_sheets_manager

from src.tgbot.dialogs.states import CompanySelection
from src.tgbot.enums import ExcelColumn
from src.tgbot.utils import chart_factory
from src.tgbot.managers import task_runner


async def select_spreadsheet_callback(
    callback_query: CallbackQuery,  # noqa
    widget: Select,  # noqa
    dialog_manager: DialogManager,
    item_id: str,
):
    dialog_manager.dialog_data["spreadsheet_idx"] = item_id
    await dialog_manager.switch_to(CompanySelection.company_selection)


async def select_company_callback(
    callback_query: CallbackQuery,  # noqa
    widget: Select,  # noqa
    dialog_manager: DialogManager,
    item_id: int,
):
    dialog_manager.dialog_data["company_idx"] = item_id
    await dialog_manager.switch_to(CompanySelection.metric_type_selection)


async def select_metric_type_callback(
    callback_query: CallbackQuery,  # noqa
    widget: Select,  # noqa
    dialog_manager: DialogManager,
    item_id: str,
):
    dialog_manager.dialog_data["metric_type_name"] = item_id
    await dialog_manager.switch_to(CompanySelection.chart_selection)


async def select_chart_type_callback(
    callback_query: CallbackQuery,
    widget: Select,  # noqa
    dialog_manager: DialogManager,
    item_id: str,  # chart type name
):
    spreadsheet_idx = dialog_manager.dialog_data.get("spreadsheet_idx")
    company_idx = dialog_manager.dialog_data.get("company_idx")
    metric_type = dialog_manager.dialog_data.get("metric_type_name")

    companies = await google_sheets_manager.get_spreadsheet_tables(
        spreadsheet_idx=spreadsheet_idx
    )

    table_name = companies[int(company_idx)]
    column_letter = ExcelColumn[metric_type].value

    data = await google_sheets_manager.get_data(
        spreadsheet_idx=spreadsheet_idx,
        table_name=table_name,
        column_start=column_letter,
        column_end=column_letter,
    )

    chart_bytes = await task_runner.run_chart_generation(
        chart_factory.generate_chart, item_id, data
    )

    await callback_query.message.answer_photo(
        photo=BufferedInputFile(
            file=chart_bytes,
            filename=f"{item_id}.png",
        )
    )
