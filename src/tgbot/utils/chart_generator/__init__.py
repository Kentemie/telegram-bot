from typing import Any
from collections import defaultdict

from src.tgbot.enums import ChartType

from .base import ChartGenerator
from .plots import (
    AreaPlotGenerator,
    BarChartGenerator,
    LinePlotGenerator,
    ScatterPlotGenerator,
)


class ChartFactory:
    def __init__(self):
        self._generators = {
            ChartType.area_plot.name: AreaPlotGenerator(),
            ChartType.bar_chart.name: BarChartGenerator(),
            ChartType.line_plot.name: LinePlotGenerator(),
            ChartType.scatter_plot.name: ScatterPlotGenerator(),
        }

    def generate_chart(self, chart_type: str, data: Any) -> bytes:
        generator: ChartGenerator = self._generators.get(chart_type)

        if not generator:
            raise ValueError(f"Chart type {chart_type} not supported.")

        parsed_data = self._parse_data(data)

        return generator.generate(
            parsed_data[0],
            title=f"{parsed_data[1][1]} по месяцам",
            xlabel=f"{parsed_data[1][1]}",
            ylabel=f"{parsed_data[1][0]}",
        )

    def _parse_data(  # noqa
        self, raw_data: list[list[list[str]]]
    ) -> tuple[dict[str, list[str]], list[str]]:
        headers_to_values = defaultdict(list)
        headers = []

        for columns in raw_data:
            for idx, header in enumerate(columns[0]):
                header = header.strip().replace(",", "")
                headers.append(header)

                for values in columns[1:]:
                    headers_to_values[header].append(
                        values[idx].strip().replace(",", "")
                    )

        return headers_to_values, headers


chart_factory = ChartFactory()
