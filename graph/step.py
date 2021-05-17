from __future__ import annotations

from typing import List


class Step:
    value: int = None

    def __init__(self, value: int):
        self.value = value

    def increase(self, percentage: float) -> None:
        self.value += self.value * percentage

    def new_increase(self, percentage: float) -> Step:
        return Step(int(self.value + self.value * percentage))

    def growth(self, percentage: float, iterations: int) -> List[Step]:
        initial = self
        return [initial, *(initial := initial.new_increase(percentage) for _ in range(iterations))]
