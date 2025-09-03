import json
from typing import Any

import pandas as pd

from read_data import read_xlsx_file
from utils import get_data_in_period


def cashback_categories(year: str, month: str, data: pd.DataFrame = read_xlsx_file()) -> json:
    pass


def investment_bank(month: str, transactions: list[dict[str, Any]], limit: int) -> float:
    pass
