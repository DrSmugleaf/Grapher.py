from unittest import TestCase, skip

from graph import grapher
from graph.step import Step


class TestGraph(TestCase):
    def test_hundred(self):
        step = Step(1000)
        growth = step.growth(percentage=0.1, iterations=100)
        grapher.plot([s.value for s in growth])
        grapher.show()

    def test_hundred_modified(self):
        step = Step(1000)
        growth = step.growth(percentage=0.1, iterations=3)

        halving = growth[3]
        halving.value /= 2
        halved_growth = halving.growth(percentage=0.05, iterations=6)

        final_growth = growth[:3] + halved_growth

        grapher.plot([s.value for s in final_growth])
        grapher.show()
