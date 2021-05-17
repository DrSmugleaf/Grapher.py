from unittest import TestCase

from graph.step import Step


class TestStep(TestCase):
    def test_increase(self):
        step = Step(1000)
        step.increase(0.1)

        self.assertEqual(1100, step.value)

    def test_new_increase(self):
        step = Step(1000)
        new = step.new_increase(0.1)

        self.assertEqual(1000, step.value)
        self.assertEqual(1100, new.value)

    def test_growth(self):
        step = Step(1000)
        growth = step.growth_percentage(percentage=0.1, iterations=3)

        self.assertEqual([1000, 1100, 1210, 1331], [s.value for s in growth])
