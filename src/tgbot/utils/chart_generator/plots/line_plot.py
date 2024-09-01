import matplotlib.pyplot as plt

from src.tgbot.utils.chart_generator.base import ChartGenerator


class LinePlotGenerator(ChartGenerator):
    def generate(
        self, data, title: str = "", xlabel: str = "", ylabel: str = ""
    ) -> bytes:
        plt.figure()
        plt.plot(data[xlabel], data[ylabel], marker="o", linestyle="-", color="b")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)

        return self._save_to_bytes()
