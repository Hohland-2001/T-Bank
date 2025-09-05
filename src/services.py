import json
from typing import Any

from read_data import read_xlsx_file


def search(words: str = None) -> Any:
    """Функция возвращает json-ответ с найденным словом пользователя в описании или категории операции"""
    if words is None:
        return []
    else:
        df = read_xlsx_file()
        n = 0
        index = list(df.columns)
        all_list = []
        for i, row in df.iterrows():
            if words in str(row.tolist()):
                all_dict = {}
                for ind in index:
                    max_n = len(list(row))
                    if n <= max_n - 1:
                        all_dict[ind] = list(row)[n]
                        all_list.append(all_dict)
                        n += 1
            else:
                continue
        json_response = json.dumps(all_list, ensure_ascii=False, indent=4)
        return json_response
