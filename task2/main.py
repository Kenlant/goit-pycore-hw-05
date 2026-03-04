import re
from typing import Callable

test_text = """За понеділок магазин отримав дохід 1250.50 від продажу ноутбуків.
У вівторок додатковий прибуток склав 340.75 від аксесуарів.
У середу клієнти придбали товарів на суму 89.99 та 120.00
Номер накладної 45821 не є доходом.
У четвер зафіксовано прибуток 560.40 від продажу моніторів.
У пʼятницю невеликий дохід 45.50 від кабелів та 78.25 від адаптерів."""


def generator_numbers(text):
    for x in re.findall(r"\s\d+.\d+?\s", text):
        yield float(x.strip())


def sum_profit(text: str, func: Callable):
    return sum(func(text))


if (__name__ == "__main__"):
    total_income = sum_profit(test_text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
