import json
import logging
import os

import pandas as pd

log_file_path = os.path.join(os.path.dirname(__file__), "../logs/read_data.log")
logger = logging.getLogger("read_data")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{log_file_path}", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_xlsx_file(path_to_excel: str = "../data/operations.xlsx") -> pd.DataFrame | None:
    """Функция читает excel-файл и возвращает двумерную таблицу"""
    try:
        df = pd.read_excel(path_to_excel, sheet_name="Отчет по операциям")
        logger.info(f"Функция обработала таблицу")
        return df
    except Exception as e:
        print(f"Произошла ошибка {e}")
        logger.error(f"Произошла ошибка {e}")
        return None


def read_json_file(path_to_file: str = "../data/user_settings.json") -> dict | None:
    """Функция читает json-файл и возвращает словарь"""
    try:
        if path_to_file[-5:] == ".json":
            with open(path_to_file, "r", encoding="utf-8") as f:
                user_settings = json.load(f)
        else:
            with open(path_to_file) as f:
                user_settings = f
        logger.info(f"Функция прочитала json-файл")
        return user_settings
    except Exception as e:
        print(f"Произошла ошибка {e}")
        logger.error(f"Произошла ошибка {e}")
        return None
