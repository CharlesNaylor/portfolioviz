"""
Dataclass for portfolio composition

final_tickers = {
    'NoBrainers': ['IBM', 'CSCO', 'QSR', 'LMT', 'PG', 'MYL', 'TXN', 'T', 'PEP', 'JCI'],
        'FurtherAfield': ['RCKY', 'GPX', 'MLR', 'ATAX', 'SANM', 'DHI', 'XRX', 'DRH']
        }
"""
import datetime
import json
import logging

from dataclasses import asdict, dataclass
from decimal import Decimal
from pathlib import Path
from typing import List

from utils.encoder import PortfolioEncoder

logger = logging.getLogger(__name__)


@dataclass
class Portfolio:
    """class for keeping track of portfolio elements"""

    name: str
    starting_nav: Decimal
    starting_date: datetime.date
    tickers: List[str]

    @classmethod
    def from_path(cls, path: Path):
        """load portfolio from json path"""
        logger.info("Reading from %s", path)
        with open(Path(path), "r") as file_path:
            vals = json.load(file_path)
        vals["starting_nav"] = Decimal(vals["starting_nav"])
        vals["starting_date"] = datetime.datetime.strptime(
            vals["starting_date"], "%Y-%m-%d"
        ).date()
        return cls(**vals)

    def to_json(self, path: Path):
        """serialize to json"""
        with open(Path(path), "w") as file_path:
            json.dump(asdict(self), fp=file_path, cls=PortfolioEncoder)
        logger.info("Wrote %s to %s", self.name, path)
