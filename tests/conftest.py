import pytest
import datetime
import pandas as pd


@pytest.fixture
def df_transactions() -> pd.DataFrame:
    transactions = {
        'Дата операции': [
            datetime.datetime.strptime('12.11.2005 14:05:44', '%d.%m.%Y %H:%M:%S'),
            datetime.datetime.strptime('08.11.2005 22:49:26', '%d.%m.%Y %H:%M:%S'),
            datetime.datetime.strptime('11.11.2005 22:49:26', '%d.%m.%Y %H:%M:%S'),
            datetime.datetime.strptime('05.11.2005 22:49:26', '%d.%m.%Y %H:%M:%S')
        ],
        'Дата платежа': [
            datetime.datetime.strptime('12.11.2005', '%d.%m.%Y'),
            datetime.datetime.strptime('08.11.2005', '%d.%m.%Y'),
            datetime.datetime.strptime('11.11.2005', '%d.%m.%Y'),
            datetime.datetime.strptime('05.11.2005', '%d.%m.%Y'),
        ],
        "Номер карты": ['*7856', '*6345', '*2544', '*5612'],
        'Статус': ['OK', 'OK', 'OK', 'OK'],
        'Сумма операции': [-165.89, -862.46, -352.62, -32.75],
        'Валюта операции': ['RUB', 'RUB', 'RUB', 'RUB'],
        'Сумма платежа': [-165.89, -862.46, -352.62, -32.75],
        'Валюта платежа': ['RUB', 'RUB', 'RUB', 'RUB'],
        'Кэшбэк': [0.00, 0.00, 0.00, 0.00],
        'Категрия': ['Супермаркет', 'Каршеринг', 'Переводы', 'Дом и ремонт'],
        'МСС': ['5412', '8624', '7265', '3541'],
        'Описание': ['wrw', 'dfk', 'nnk', 'ienn'],
        'Бонусы(включая кэшбэк)': [2.00, 9.00, 6.00, 4.00],
        'Округление на инвесткопилку': [0.00, 0.00, 0.00, 0.00],
        'Сумма операции с округлением': [165.89, 862.46, 352.62, 32.75]
    }
    df = pd.DataFrame(transactions)
    return df
