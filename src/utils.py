import datetime
import os

import pandas as pd
import requests
from dotenv import load_dotenv

from read_data import read_json_file, read_xlsx_file


def greeting() -> str:
    """Функция возвращает приветствие в зависимости от текущего времени"""
    date_now = datetime.datetime.now().strftime("%H")
    result = ""
    if date_now in ["01", "02", "03", "04", "05", "06"]:
        result += "Доброй ночи"
    elif date_now in ["07", "08", "09", "10", "11", "12"]:
        result += "Доброе утро"
    elif date_now in ["13", "14", "15", "16", "17", "18"]:
        result += "Добрый день"
    elif date_now in ["19", "20", "21", "22", "23", "00"]:
        result += "Добрый вечер"
    return result


def get_list_cards(date_time: str) -> list:
    """Функция получает дату и выдаёт информацию по каждой карте от начала месяца до заданной даты"""
    df = get_data_in_period(date_time)
    all_list = []
    for i in range(len(get_list_last_digits(df))):
        all_dict = {}
        all_dict["last_digits"] = get_list_last_digits(df)[i]
        all_dict["total_spent"] = get_list_total_spent(df)[i]
        all_dict["cashback"] = get_list_cashback(df)[i]
        all_list.append(all_dict)
    return all_list


def get_data_in_period(
    date_time: str = None, date_format: str = "%Y-%m-%d %H:%M:%S", df: pd.DataFrame = read_xlsx_file()
) -> pd.DataFrame:
    """Функция получает дату и возвращает таблицу данных за период с начала месяца по заданную дату"""
    if date_time is None:
        return df
    else:
        end_date = datetime.datetime.strptime(date_time, date_format)
        start_date = end_date.replace(day=1, hour=00, minute=00, second=00)
        list_date = [start_date.strftime("%d.%m.%Y %H:%M:%S"), end_date.strftime("%d.%m.%Y %H:%M:%S")]
        df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
        start_date = datetime.datetime.strptime(list_date[0], "%d.%m.%Y %H:%M:%S")
        end_date = datetime.datetime.strptime(list_date[1], "%d.%m.%Y %H:%M:%S")
        filtered_df = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]
        return filtered_df


def get_list_last_digits(df: pd.DataFrame) -> list:
    """Функция получает DataFrame и возвращает список номеров карт без *"""
    df_not_null = df.loc[df["Номер карты"].notnull()]
    card_list_new = []
    card_list = []
    for i in df_not_null.iloc[:, 2]:
        if i in card_list:
            continue
        else:
            card_list.append(i)
    for element in card_list:
        element_new = element.replace("*", "")
        card_list_new.append(element_new)
    return card_list_new


def get_list_total_spent(df: pd.DataFrame) -> list:
    """Функция получает DataFrame и возвращает список трат по каждой карте"""
    df_not_null = df.loc[df["Номер карты"].notnull()]
    max_index = df_not_null.shape[0]
    count_total = 0
    index = 0
    list_total_spent = []
    card_list = []
    for i in df_not_null.iloc[:, 2]:
        if i in card_list:
            continue
        else:
            card_list.append(i)
    for card in card_list:
        while index < max_index:
            for i in df_not_null.iloc[:, 2]:
                if i == card:
                    count_total += float(df_not_null.iloc[index, 4] * -1)
                    index += 1
                else:
                    index += 1
            list_total_spent.append(round(count_total, 2))
        else:
            index = 0
    return list_total_spent


def get_list_cashback(df: pd.DataFrame) -> list:
    """Функция получает DataFrame и возвращает список кэшбэка по карте"""
    list_total_spent = get_list_total_spent(df)
    list_cashback = []
    for i in list_total_spent:
        cashback = i / 100
        list_cashback.append(round(cashback, 2))
    return list_cashback


def get_list_top_transactions(date_time: str = None):
    """Функция получает дату и выдаёт топ-5 транзакций от начала месяца до заданной даты"""
    df = get_data_in_period(date_time)
    df_not_null = df.loc[df["Номер карты"].notnull()]
    df_top_amount = df_not_null.nlargest(5, "Сумма операции с округлением")
    list_top_amount = []
    list_top_date = []
    list_top_category = []
    list_top_description = []
    all_list = []
    for i, row in df_top_amount.items():
        if i == "Сумма операции с округлением":
            for r in row:
                list_top_amount.append(r)
        elif i == "Дата операции":
            for r in row:
                list_top_date.append(r.strftime("%d.%m.%Y"))
        elif i == "Категория":
            for r in row:
                list_top_category.append(r)
        elif i == "Описание":
            for r in row:
                list_top_description.append(r)
    for n in range(len(list_top_date)):
        all_dict = {}
        all_dict["date"] = list_top_date[n]
        all_dict["amount"] = list_top_amount[n]
        all_dict["category"] = list_top_category[n]
        all_dict["description"] = list_top_description[n]
        all_list.append(all_dict)
    return all_list


def get_currency_rates() -> list | None:
    """Функция возвращает курсы валют, заданные пользователем в user_settings.json"""
    try:
        user_currency = read_json_file()["user_currencies"]
        all_list = []

        load_dotenv(".env")
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": API_KEY}

        for i in user_currency:
            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?" f"to={"RUB"}&from={i}&amount=1",
                headers=headers,
            )

            all_dict = {}
            all_dict["currency"] = i
            all_dict["rate"] = float(round(response.json()["result"], 2))
            all_list.append(all_dict)
        return all_list
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


def get_stock_prices() -> list | None:
    """Функция возвращает курсы акций, заданные пользователем в user_settings.json"""
    try:
        user_currency = read_json_file()["user_stocks"]
        all_list = []
        API_KEY = "DAxlMjchHZl9d2Tq9ZOYB3nbWLrXsRpR"
        for i in user_currency:
            url = "https://financialmodelingprep.com/stable/quote-short?" f"symbol={i}&apikey={API_KEY}"
            response = requests.get(url)
            all_dict = {}
            all_dict["stock"] = i
            all_dict["price"] = round(response.json()[0]["price"], 2)
            all_list.append(all_dict)
        return all_list
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None
