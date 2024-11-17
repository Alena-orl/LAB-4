# TODO решите задачу
import json
def task(filename) -> float:
    with open(filename, 'r') as file:
        data = json.load(file)

    total_sum = 0
    for item in data:
        total_sum += item["score"] * item["weight"]

    return round(total_sum, 3)

filename = "input.json"
print(task(filename))
