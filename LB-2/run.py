from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent

student1 = FullTimeStudent(name="KOLA", age=24, prac_score=910, prac_count=10, exam_scr=95, attend_pct=85)
student2 = FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20)
student3 = PartTimeStudent("CHEEV", 22, 390, 4, 78)
student4 = PartTimeStudent("YAKTAK", 21, 480, 5, 82)

university_students = [student1, student2, student3, student4]

print("Студент 1:")
print("Ім'я:", student1.name)
print("Вік:", student1.age)
print("Середній бал за практичні:", student1.avg_practice_score())
print("Загальний бал:", round(student1.total_score(), 1))

print("\nСтудент 2:")
print("Ім'я:", student2.name)
print("Вік:", student2.age)
print("Середній бал за практичні:", student2.avg_practice_score())
print("Загальний бал:", round(student2.total_score(), 1))

for student in university_students:
    student.display_info()
    if isinstance(student, FullTimeStudent):
        print(f"Загальний бал: {student.total_score()}")
    elif isinstance(student, PartTimeStudent):
        print(f"Загальний бал (заочно): {student.total_score()}")
    print("---------")
