from datetime import datetime

import pandas as pd
from src.read_data import read_xlsx_file


def spending_by_category(date: str | datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                         transactions: pd.DataFrame = read_xlsx_file(),
                         category: str = None,
                         ) -> int | None:
    try:
        df = transactions
        end_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        start_date = end_date.replace(month=int(end_date.strftime('%m')) - 2, day=1, hour=00, minute=00, second=00)
        list_date = [start_date.strftime("%d.%m.%Y %H:%M:%S"), end_date.strftime("%d.%m.%Y %H:%M:%S")]
        df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
        start_date = datetime.strptime(list_date[0], "%d.%m.%Y %H:%M:%S")
        end_date = datetime.strptime(list_date[1], "%d.%m.%Y %H:%M:%S")
        filtered_df = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]
        result_df = filtered_df[filtered_df['Категория'] == category]
        return result_df
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None
