import io
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod


class ChartGenerator(ABC):
    @abstractmethod
    def generate(
        self, data, title: str = "", xlabel: str = "", ylabel: str = ""  # noqa
    ) -> bytes:
        pass

    def _save_to_bytes(self) -> bytes:  # noqa
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close()
        return buf.getvalue()
