#Задание №2: Конвертер из CSV в JSON формат
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json() -> None:
    """Конвертер из CSV в JSON формат"""

    with open(INPUT_FILENAME, "r") as in_file:
        csv_data = [data for data in csv.DictReader(in_file)]

    with open(OUTPUT_FILENAME, "w") as out_file:
        json.dump(csv_data, out_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    csv_to_json()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")