from pathlib import Path
from collections import Counter
import re
import sys


def parse_log_line(line: str) -> dict:
    match = re.search(r"(\d+-\d+-\d+)\s(\d+:\d+:\d+)\s(\w+)\s(.+)", line)
    if (match == None):
        return None
    if (len(match.groups()) != 4):
        return None

    result = {}
    result["date"] = match.group(1)
    result["time"] = match.group(2)
    result["level"] = match.group(3)
    result["message"] = match.group(4)
    result["full_message"] = match.group()

    return result


def load_logs(file_path: str):
    path = Path(file_path)
    if (not path.exists()):
        return None

    with path.open("r") as f:
        return [x for x in f]


def count_logs_by_level(logs: list):
    levels = [x["level"] for x in logs]
    return Counter(levels)


def filter_logs_by_level(logs: list, level: str):
    return list(filter(lambda x: x["level"].casefold() == level.casefold(), logs))


def display_statistic(log_counts: dict):
    col1_header = "Рівень логування"
    col2_header = "Кількість"

    col1_width = max(len(col1_header), max(len(k) for k in log_counts))
    col2_width = max(len(col2_header), max(len(str(v))
                     for v in log_counts.values()))

    print(f"{col1_header:<{col1_width}} | {col2_header:<{col2_width}}")

    print(f"{'-'*col1_width}-+-{'-'*col2_width}")

    for level, count in log_counts.items():
        print(f"{level:<{col1_width}} | {count:<{col2_width}}")


def display_messages(logs: list, level: str):
    if (len(logs) == 0):
        print(f"Немає записів з рівнем важливості '{level}'")
        return

    print(f"Деталі логів для рівня '{level}':")
    for x in logs:
        print(x["full_message"])


def main():
    if (len(sys.argv) < 2):
        print("Вкажіть шлях до файлу!")
        return

    file_path = sys.argv[1]

    level = ""
    if (len(sys.argv) > 2):
        level = sys.argv[2]

    logs = load_logs(file_path)
    if (logs == None):
        print("Файл не знайдено")
        return

    parsed_logs = [parse_log_line(x) for x in logs]

    if (any(x == None for x in parsed_logs)):
        print("Невірний формат файлу")
        return

    logs_by_log_level = count_logs_by_level(parsed_logs)
    display_statistic(logs_by_log_level)

    if (level == ""):
        return

    print()

    filtered_logs = filter_logs_by_level(parsed_logs, level)
    display_messages(filtered_logs, level)


if (__name__ == "__main__"):
    main()
