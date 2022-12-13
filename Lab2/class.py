from random import randint, choice


class Person:
    def __init__(self):
        self.name = choice(['Jim', 'Tom', 'Nick', 'Ann'])
        self.age = randint(1, 80)
