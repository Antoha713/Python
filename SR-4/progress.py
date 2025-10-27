from abc import ABC, abstractmethod

class Progress(ABC):
    def __init__(self, subjects: list, grades: list):
        self.subjects = subjects
        self.grades = grades