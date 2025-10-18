import json
import logging
import os
from typing import Any

import pandas as pd

from src.read_data import read_xlsx_file

log_file_path = os.path.join(os.path.dirname(__file__), "../logs/services.log")
logger = logging.getLogger("services")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{log_file_path}", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def search(words: str | None = None, df: pd.DataFrame | None = None) -> Any:
    """Функция возвращает json-ответ с найденным словом пользователя в описании или категории операции"""
    try:
        if words is None or words == "":
            logger.info(f"Слово не задано. Возвращется пустой список")
            return []
        else:
            # df = read_xlsx_file()
            index = list(df.columns)
            all_list = []
            logger.info(f"Поиск совпадений начался...")
            for i, row in df.iterrows():
                n = 0
                max_n = len(row.tolist())
                if words.lower() in str(row.tolist()).lower():
                    all_dict = {}
                    for ind in index:
                        if n <= max_n:
                            all_dict[ind] = row.tolist()[n]
                            n += 1
                    all_list.append(all_dict)
            json_response = json.dumps(all_list, ensure_ascii=False, indent=4)
            logger.info(f"Поиск завершён. Количество результатов {len(all_list)}")
            return json_response
    except Exception as e:
        print(f"Произошла ошибка {e}")
        logger.error(f"Произошла ошибка {e}")
        return None
