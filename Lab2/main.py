import json
from my_class import *


def load_to_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def write_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


data = {"Persons": []}

for i in range(10):
    data['Persons'].append(Person().__dict__)

write_to_json(data, 'data.json')
read = load_to_json('data.json')
print('Имя второго человека и возраст третьего')
print(read['Persons'][1]['name'], read['Persons'][2]['age'])