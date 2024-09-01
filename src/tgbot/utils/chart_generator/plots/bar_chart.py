import matplotlib.pyplot as plt

from src.tgbot.utils.chart_generator.base import ChartGenerator


class BarChartGenerator(ChartGenerator):
    def generate(
        self, data, title: str = "", xlabel: str = "", ylabel: str = ""
    ) -> bytes:
        plt.figure()
        plt.bar(data[xlabel], data[ylabel], color="g")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)

        return self._save_to_bytes()
