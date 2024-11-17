# TODO импортировать необходимые молули

import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file) -> None:
    json_data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            json_data.append(row)

    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
task(INPUT_FILENAME)
