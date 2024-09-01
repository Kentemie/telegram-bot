from aiogram_dialog import DialogManager

from src.core.services.google import google_sheets_manager

from src.tgbot.schemas import Sheet, Company
from src.tgbot.enums import MetricType, ChartType


async def get_spreadsheets(dialog_manager: DialogManager, **kwargs):  # noqa
    spreadsheets: list[tuple[str, str]] = await google_sheets_manager.get_spreadsheets()

    return {
        "spreadsheets": [
            Sheet(id=idx, sheet_id=pk, sheet_name=name)
            for idx, (pk, name) in enumerate(spreadsheets)
        ]
    }


async def get_companies(dialog_manager: DialogManager, **kwargs):  # noqa
    spreadsheet_idx = dialog_manager.dialog_data.get("spreadsheet_idx")

    companies = await google_sheets_manager.get_spreadsheet_tables(
        spreadsheet_idx=spreadsheet_idx
    )

    return {
        "companies": [Company(id=idx, name=name) for idx, name in enumerate(companies)]
    }


async def get_metric_types(dialog_manager: DialogManager, **kwargs):  # noqa
    return {
        "metric_types": [
            (MetricType.revenue.name, MetricType.revenue.value),
            (MetricType.expenses.name, MetricType.expenses.value),
            (MetricType.profit.name, MetricType.profit.value),
            (
                MetricType.corporate_income_tax.name,
                MetricType.corporate_income_tax.value,
            ),
        ]
    }


async def get_chart_types(dialog_manager: DialogManager, **kwargs):  # noqa
    return {
        "chart_types": [
            (ChartType.area_plot.name, ChartType.area_plot.value),
            (ChartType.bar_chart.name, ChartType.bar_chart.value),
            (ChartType.line_plot.name, ChartType.line_plot.value),
            (ChartType.scatter_plot.name, ChartType.scatter_plot.value),
        ]
    }
