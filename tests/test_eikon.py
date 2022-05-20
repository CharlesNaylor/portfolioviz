"""Tests for the eikon connector"""

import unittest

from pipeline.eikon import Eikon


class TestEikon(unittest.TestCase):
    """tests for the eikon connector"""

    def setUp(self):
        self.ric = ["IBM.O", "CSCO.O"]
        self.fields = ["OPEN", "HIGH", "LOW", "CLOSE", "VOLUME"]

    def test_history(self):
        eik = Eikon()
        df = eik.get_timeseries(rics=self.ric, fields=self.fields)
        breakpoint()
