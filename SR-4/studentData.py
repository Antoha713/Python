from progress import Progress
from desiredProgress import DesiredProgress
from student import Student

class StudentData:
    def __init__(self, student: Student, real_perf: Progress, desired_perf: DesiredProgress):
        self.student = student
        self.real_perf = real_perf
        self.desired_perf = desired_perf

    def get_data(self):
        return {
            "PIB": self.student.get_pib(),
            "Group": self.student.get_group_number(),
            "BirthDate": self.student.get_birth_date(),
            "Address": self.student.get_address(),
            "Subjects": self.real_perf.subjects,
            "RealGrades": self.real_perf.grades,
            "RealAvg": self.real_perf.average_grade(),
            "DesiredGrades": self.desired_perf.grades,
            "DesiredAvg": self.desired_perf.average_grade()
        }