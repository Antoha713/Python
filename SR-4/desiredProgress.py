from progress import Progress

class DesiredProgress(Progress):
    def __init__(self, subjects: list, grades: list, desired_avg: float = None):
        super().__init__(subjects, grades)
        self.desired_avg = desired_avg

    def average_grade(self):

        if self.desired_avg is not None:
            return self.desired_avg
        return sum(self.grades) / len(self.grades)