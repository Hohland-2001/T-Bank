import json
from typing import Any

from src.utils import get_currency_rates, get_list_cards, get_list_top_transactions, get_stock_prices, greeting


def main_func(date_time: str | None = None) -> Any:
    """
    Функцию принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращающую JSON-ответ
    """
    response = {
        "greeting": f"{greeting()}",
        "cards": get_list_cards(date_time),
        "top_transactions": get_list_top_transactions(date_time),
        "currency_rates": get_currency_rates(),
        "stock_prices": get_stock_prices(),
    }
    json_response = json.dumps(response, ensure_ascii=False, indent=4)
    return json_response


print(main_func("2021-08-14 18:50:16"))
