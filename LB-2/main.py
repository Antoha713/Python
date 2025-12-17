from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name  # Зберігає в параметри ім'я особи.
        self.age = age    # Зберігає вік особи.
