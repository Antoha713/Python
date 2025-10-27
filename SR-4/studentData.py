from progress import Progress
from desiredProgress import DesiredProgress
from student import Student

class StudentData:
    def __init__(self, student: Student, real_perf: Progress, desired_perf: DesiredProgress):
        self.student = student
        self.real_perf = real_perf
        self.desired_perf = desired_perf