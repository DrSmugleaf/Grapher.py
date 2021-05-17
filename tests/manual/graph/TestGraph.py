from unittest import TestCase

from graph import grapher
from graph.step import Step


folder = "../../../images/"


class TestGraph(TestCase):

    def test_hundred(self):
        step = Step(1000)
        growth = step.growth_percentage(percentage=0.1, iterations=100)
        grapher.plot([s.value for s in growth])
        grapher.save(folder + "test_hundred.png")

    def test_hundred_modified(self):
        step = Step(1000)
        growth = step.growth_percentage(percentage=0.1, iterations=3)

        halving = growth[3]
        halving.value /= 2
        halved_growth = halving.growth_percentage(percentage=0.05, iterations=6)

        final_growth = growth[:3] + halved_growth

        grapher.plot([s.value for s in final_growth])
        grapher.save(folder + "test_hundred_modified.png")
