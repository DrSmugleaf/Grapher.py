from __future__ import annotations

from typing import List, Callable


class Step:
    value: int = None

    def __init__(self, value: int):
        self.value = value

    def increase(self, percentage: float) -> None:
        self.value += self.value * percentage

    def new_increase(self, percentage: float) -> Step:
        return Step(int(self.value + self.value * percentage))

    def growth_percentage(self, percentage: float, iterations: int) -> List[Step]:
        return self.growth(lambda s: s.new_increase(percentage), iterations)

    def growth(self, func: Callable[[Step], Step], iterations: int) -> List[Step]:
        initial = self
        return [initial, *(initial := func(initial) for _ in range(iterations))]
