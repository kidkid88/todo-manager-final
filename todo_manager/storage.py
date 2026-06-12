import json


def save_to_json(tasks, filename):
    data = []

    for task in tasks:
        data.append(task.__dict__)

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )