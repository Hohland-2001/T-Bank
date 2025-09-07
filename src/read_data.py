import json

import pandas as pd


def read_xlsx_file(path_to_excel: str = "../data/operations.xlsx") -> pd.DataFrame | None:
    """Функция читает excel-файл и возвращает двумерную таблицу"""
    try:
        df = pd.read_excel(path_to_excel, sheet_name="Отчет по операциям")
        return df
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


def read_json_file(path_to_json: str = "../data/user_settings.json") -> dict | None:
    """Функция читает json-файл и возвращает словарь"""
    try:
        with open(path_to_json) as f:
            user_settings = json.load(f)
        return user_settings
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None
