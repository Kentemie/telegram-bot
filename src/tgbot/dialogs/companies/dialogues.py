from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Back, Cancel, Column, ScrollingGroup, Select, Row

from src.tgbot.dialogs.states import CompanySelection
from src.tgbot.dialogs.companies.callbacks import (
    select_spreadsheet_callback,
    select_company_callback,
    select_metric_type_callback,
    select_chart_type_callback,
)
from src.tgbot.dialogs.companies.getters import (
    get_spreadsheets,
    get_companies,
    get_metric_types,
    get_chart_types,
)
from src.tgbot.dialogs.callbacks import close_dialog


company_selection_dialog = Dialog(
    Window(
        Const("Please select a spreadsheet:"),
        Select(
            text=Format("{item.sheet_name}"),
            id="spreadsheet_selection",
            item_id_getter=lambda item: item.id,
            items="spreadsheets",
            on_click=select_spreadsheet_callback,
        ),
        Back(
            Const("⬅️ Main menu"),
            on_click=close_dialog,
        ),
        state=CompanySelection.spreadsheet_selection,
        getter=get_spreadsheets,
    ),
    Window(
        Const("Please select a company:"),
        ScrollingGroup(
            Select(
                text=Format("{item.name}"),
                id="company_selection",
                item_id_getter=lambda item: item.id,
                items="companies",
                on_click=select_company_callback,
            ),
            Back(
                Const("⬅️ Back"),
            ),
            id="companies_group",
            height=4,
            width=2,
            hide_on_single_page=True,
        ),
        state=CompanySelection.company_selection,
        getter=get_companies,
    ),
    Window(
        Const("Please select the metric type you want to get a report on:"),
        Column(
            Select(
                text=Format("{item[1]}"),
                id="metric_type_selection",
                item_id_getter=lambda item: item[0],
                items="metric_types",
                on_click=select_metric_type_callback,
            ),
        ),
        Back(
            Const("⬅️ Back"),
        ),
        state=CompanySelection.metric_type_selection,
        getter=get_metric_types,
    ),
    Window(
        Const("Please select a chart type:"),
        Column(
            Select(
                text=Format("{item[1]}"),
                id="chart_type_selection",
                item_id_getter=lambda item: item[0],
                items="chart_types",
                on_click=select_chart_type_callback,
            ),
        ),
        Row(
            Back(
                Const("⬅️ Back"),
            ),
            Cancel(
                Const("❌ Exit"),
            ),
        ),
        state=CompanySelection.chart_selection,
        getter=get_chart_types,
    ),
)
