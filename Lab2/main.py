import json


def load_to_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def write_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


