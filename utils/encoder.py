"""
Custom JSON encoder to handle dataclasses, Decimal, and dates
"""

import dataclasses
import datetime
import json
from decimal import Decimal


class PortfolioEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, Decimal):
            return str(o)
        return super().default(o)
