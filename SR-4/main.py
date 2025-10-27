from student import Student
from progress import Progress
from desiredProgress import DesiredProgress
from studentData import StudentData
from database import Database

class RealProgres(Progress):
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Іваненко Іван Іванович", "ПМ-21", "2003-05-17", "Київ")
real_perf = RealProgres(["Математика", "Фізика", "Інформатика"], [85, 90, 95])
desired_perf = DesiredProgress(["Математика", "Фізика", "Інформатика"], [95, 100, 100], desired_avg=98.3)

student_data = StudentData(student, real_perf, desired_perf)

db = Database()
db.create_table()
db.insert_student(student_data.get_data())

for row in db.show_all():
    print(row)

db.close()