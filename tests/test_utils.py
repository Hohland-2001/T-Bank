from unittest.mock import patch, mock_open
from src.utils import *
from src.read_data import read_json_file
import pytest


def test_get_list_card(df_transactions) -> None:
    assert get_list_cards(date_time='2005-11-18 10:45:15', df=df_transactions) == [
        {
            'cashback': 1.66,
            'last_digits': '7856',
            'total_spent': 165.89,
        },
        {
            'cashback': 8.62,
            'last_digits': '6345',
            'total_spent': 862.46,
        },
        {
            'cashback': 3.53,
            'last_digits': '2544',
            'total_spent': 352.62,
        },
        {
            'cashback': 0.33,
            'last_digits': '5612',
            'total_spent': 32.75,
        },
    ]


def test_get_data_in_period(df_transactions) -> None:
    assert get_data_in_period(df=None) == None


def test_get_list_last_digits(df_transactions) -> None:
    assert get_list_last_digits(df_transactions) == ['7856', '6345', '2544', '5612']


def test_get_list_total_spent(df_transactions) -> None:
    assert get_list_total_spent(df_transactions) == [165.89, 862.46, 352.62, 32.75]


def test_get_list_cashback(df_transactions) -> None:
    assert get_list_cashback(df_transactions) == [1.66, 8.62, 3.53, 0.33]


def test_get_list_top_transactions(df_transactions) -> None:
    assert get_list_top_transactions() is None
    assert get_list_top_transactions('2005-11-09 10:45:15') == []


@patch('requests.get')
def test_get_currency_rates(mock_get) -> None:
    mock_get.return_value.json.return_value = {
        "result": 80.85
    }
    assert get_currency_rates() == [
        {
            "currency": "USD",
            "rate": 80.85
        },
        {
            "currency": "EUR",
            "rate": 80.85
        }
    ]


@patch('requests.get')
def test_get_stock_prices(mock_get):
    mock_get.return_value.json.return_value = [{"price": 2.05}]
    assert get_stock_prices() == [
        {
            'price': 2.05,
            'stock': 'AAPL',
        },
        {
            'price': 2.05,
            'stock': 'AMZN',
        },
        {
            'price': 2.05,
            'stock': 'GOOGL',
        },
        {
            'price': 2.05,
            'stock': 'MSFT',
        },
        {
            'price': 2.05,
            'stock': 'TSLA',
        },
    ]
