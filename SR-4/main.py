from student import Student
from progress import Progress
from desiredProgress import DesiredProgress
from studentData import StudentData
from database import Database

class RealProgres(Progress):
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Іваненко Іван Іванович", "ПМ-21", "2003-05-17", "Київ")
real_perf1 = RealProgres(["Математика", "Фізика", "Інформатика"], [85, 90, 95])
desired_perf1 = DesiredProgress(["Математика", "Фізика", "Інформатика"], [95, 100, 100])

student2 = Student("Дуб Василь Іванович", "КН-22", "2004-02-14", "Київ")
real_perf2 = RealProgres(["Українська", "Фізика", "Філософія"], [60, 74, 100])
desired_perf2 = DesiredProgress(["Українська", "Фізика", "Філософія"], [85, 75, 90])

student_data1 = StudentData(student1, real_perf1, desired_perf1)
student_data2 = StudentData(student2, real_perf2, desired_perf2)

db = Database()
db.create_table()
db.insert_student(student_data1.get_data())
db.insert_student(student_data2.get_data())

for row in db.show_all():
    print(row)

db.close()