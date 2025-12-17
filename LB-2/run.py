from FullTimeStudent import FullTimeStudent

student1 = FullTimeStudent(name="KOLA", age=24,
                           prac_score=910, prac_count=10,
                           exam_scr=95, attend_pct=85)

student2 = FullTimeStudent(name="Klavdia Petrivna", age=19,
                           prac_score=930, prac_count=10,
                           exam_scr=99, attend_pct=20)

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
