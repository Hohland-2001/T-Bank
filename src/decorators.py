def log(name_file: str = '../report.txt'):
    def wrapper(func):
        def inner(*args, **kwargs):
            with open(f'../reports/{name_file}', 'w', encoding='utf-8') as file:
                file.write(func(*args, **kwargs))
            return None
        return inner
    return wrapper