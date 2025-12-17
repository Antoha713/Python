class Person:
    def __init__(self, name, surname, grade=1):
        self.name = name
        self.surname = surname
        self.grade = grade

    def get_info(self):
        return f"Студент: {self.name} {self.surname}, оцінка: {self.grade}"

    def __del__(self):
        print(f"Ви отримали стипендію {self.name} {self.surname}")


p1 = Person("Іван", "Петренко", 5)
p2 = Person("Олена", "Коваль", 4)
p3 = Person("Андрій", "Шевченко")  # оцінка за замовчуванням = 1


