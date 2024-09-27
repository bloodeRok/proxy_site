from dataclasses import dataclass


@dataclass
class PlotData:
    points: dict[str, int]
    title: str = ""
