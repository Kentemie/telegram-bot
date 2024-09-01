from enum import Enum


class MetricType(Enum):
    revenue = "revenue"
    expenses = "expenses"
    profit = "profit"
    corporate_income_tax = "corporate_income_tax"


class ExcelColumn(Enum):
    revenue = "B"
    expenses = "C"
    profit = "D"
    corporate_income_tax = "E"


class ChartType(Enum):
    area_plot = "area_plot"
    bar_chart = "bar_chart"
    line_plot = "line_plot"
    scatter_plot = "scatter_plot"
