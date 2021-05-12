from typing import List

from matplotlib import pyplot


def increase(
        amount: int,
        percentage: float
) -> int:
    return int(amount * percentage)


def total(
        amount: int,
        percentage: float
) -> int:
    return amount + increase(amount, percentage)


def get_growth(
        initial: int,
        iterations: int,
        percentage: float
) -> List[int]:
    return [initial, *(initial := total(amount=initial, percentage=percentage) for _ in range(iterations))]


def plot(
        x: List[int],
        title: str = None,
        x_label: str = "iteration",
        y_label: str = "amount",
        font_size: int = 12
):
    fig, ax = pyplot.subplots()
    ax.plot(x)

    first = x[0]
    ax.annotate(f"{first:,}", (0, first))

    last = x[-1]
    ax.annotate(f"{last:,}", (len(x), last))

    pyplot.grid(True)
    pyplot.title(title, fontsize=font_size)
    pyplot.xlabel(x_label, fontsize=font_size)
    pyplot.ylabel(y_label, fontsize=font_size)
    pyplot.tight_layout()


def show():
    pyplot.show()


def save(name: str = "images/image.png"):
    pyplot.savefig(name)
