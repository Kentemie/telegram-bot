import matplotlib.pyplot as plt

from src.tgbot.utils.chart_generator.base import ChartGenerator


class AreaPlotGenerator(ChartGenerator):
    def generate(
        self, data, title: str = "", xlabel: str = "", ylabel: str = ""
    ) -> bytes:
        plt.figure()
        plt.fill_between(data[xlabel], data[ylabel], color="skyblue", alpha=0.5)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)

        return self._save_to_bytes()
