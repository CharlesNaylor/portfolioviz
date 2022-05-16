"""
Testing for the portfolio dataclass
"""
import datetime
import logging
import unittest
from decimal import Decimal

from config.portfolio import Portfolio

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TestPortfolio(unittest.TestCase):
    """tests for the portfolio dataclass"""

    def setUp(self):
        self.tickers = [
            "IBM",
            "CSCO",
            "QSR",
            "LMT",
            "PG",
            "MYL",
            "TXN",
            "T",
            "PEP",
            "JCI",
            "RCKY",
            "GPX",
            "MLR",
            "ATAX",
            "SANM",
            "DHI",
            "XRX",
            "DRH",
        ]

    def test_encoding(self):
        p = Portfolio(
            name="TestSerial",
            starting_nav=Decimal(100),
            starting_date=datetime.date(2020, 4, 30),
            tickers=self.tickers,
        )
        p.to_json("test.json")
        ticker_str = ", ".join([f'"{x}"' for x in self.tickers])
        correct_json = f"""{{"name": "TestSerial", "starting_nav": "100", "starting_date": "2020-04-30", "tickers": [{ticker_str}]}}"""
        with open("test.json", "r") as f:
            serialized_str = f.read()
        self.assertEqual(correct_json, serialized_str)

    def test_roundtrip(self):
        p = Portfolio(
            name="TestSerial",
            starting_nav=Decimal(100),
            starting_date=datetime.date(2020, 4, 30),
            tickers=self.tickers,
        )
        p.to_json("test.json")
        new_p = Portfolio.from_path("test.json")
        self.assertEqual(p, new_p)
