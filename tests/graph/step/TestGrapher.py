from unittest import TestCase

from graph.step.grapher import *


class TestGrapher(TestCase):
    def test_increase(self):
        new = increase(amount=1000, percentage=0.1)
        self.assertEqual(100, new)

    def test_total(self):
        new = total(amount=1000, percentage=0.1)
        self.assertEqual(1100, new)

    def test_growth(self):
        list = growth(initial=1000, percentage=0.1, iterations=3)
        self.assertEqual([1000, 1100, 1210, 1331], list)
