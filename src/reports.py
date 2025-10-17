import functools
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

import pandas as pd

from src.read_data import read_xlsx_file

log_file_path = os.path.join(os.path.dirname(__file__), "../logs/reports.log")
logger = logging.getLogger("reports")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{log_file_path}", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def save_report_flexible(filename_or_func=None) -> Any:
    """
    Гибкий декоратор, который можно использовать как с параметрами, так и без них.

    Usage:
        # Без скобок и параметров
        @save_report_flexible
        def my_report():
            return pd.DataFrame({'A': [1, 2, 3]})


        # С пустыми скобками (автоматическое имя)
        @save_report_flexible()
        def my_report():
            return pd.DataFrame({'A': [1, 2, 3]})


        # С параметром
        @save_report_flexible("custom_report.xlsx")
        def my_report():
            return pd.DataFrame({'A': [1, 2, 3]})
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)

            if not isinstance(result, pd.DataFrame):
                print(f"Предупреждение: функция {func.__name__} вернула не DataFrame. Файл не будет создан.")
                return result

            if result.empty:
                print(f"Предупреждение: функция {func.__name__} вернула пустой DataFrame. Файл не будет создан.")
                return result

            try:
                if isinstance(filename_or_func, str):
                    file_path = "../reports/" + filename_or_func
                else:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    file_path = f"../reports/report_{func.__name__}_{timestamp}.xlsx"

                Path(file_path).parent.mkdir(parents=True, exist_ok=True)
                result.to_excel(file_path, index=False, engine="openpyxl")
                print(f"Отчет успешно сохранен в файл: {file_path}")

            except Exception as e:
                print(f"Ошибка при записи отчета в файл: {e}")
                logger.error(f"Ошибка при записи отчета в файл: {e}")
            return result

        return wrapper

    if callable(filename_or_func):
        return decorator(filename_or_func)

    return decorator


@save_report_flexible("report.xlsx")
def spending_by_category(
    date: str | datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    transactions: pd.DataFrame = read_xlsx_file(),
    category: str = None,
) -> pd.DataFrame | None:
    try:
        df = transactions
        end_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        start_date = end_date.replace(month=int(end_date.strftime("%m")) - 2, day=1, hour=00, minute=00, second=00)
        list_date = [start_date.strftime("%d.%m.%Y %H:%M:%S"), end_date.strftime("%d.%m.%Y %H:%M:%S")]
        df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
        start_date = datetime.strptime(list_date[0], "%d.%m.%Y %H:%M:%S")
        end_date = datetime.strptime(list_date[1], "%d.%m.%Y %H:%M:%S")
        filtered_df = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]
        result_df = filtered_df[filtered_df["Категория"] == category]
        return result_df
    except Exception as e:
        print(f"Произошла ошибка {e}")
        logger.error(f"Произошла ошибка {e}")
        return None
