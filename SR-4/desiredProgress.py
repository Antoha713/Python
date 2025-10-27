from progress import Progress

class DesiredPerformance(Progress):
    def __init__(self, subjects: list, grades: list, desired_avg: float = None):
        super().__init__(subjects, grades)
        self.desired_avg = desired_avg
