class Employee:
    def __init__(self, name, salary, worked_days, bonus_percent=0):
        # Захищені атрибути
        self._name = name
        self._salary = salary
        self._worked_days = worked_days
        self._bonus_percent = bonus_percent

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def get_worked_days(self):
        return self._worked_days

    def set_worked_days(self, days):
        self._worked_days = days

    def get_bonus_percent(self):
        return self._bonus_percent

    def set_bonus_percent(self, percent):
        self._bonus_percent = percent

    def calculate_month_salary(self):
        return (self._salary / 30) * self._worked_days

    def calculate_bonus(self):
        return (self.calculate_month_salary() / 100) * self._bonus_percent


class Manager(Employee):
    bonus_per_worker = 100

    def __init__(self, name, salary, worked_days, bonus_percent, subordinates):
        super().__init__(name, salary, worked_days, bonus_percent)
        self._subordinates = subordinates

    def get_subordinates(self):
        return self._subordinates

    def set_subordinates(self, count):
        self._subordinates = count

    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        return base_bonus + (self._subordinates * Manager.bonus_per_worker)

    def generate_report(self):
        return f"Менеджер {self._name} керує {self._subordinates} співробітниками."

employees = []

emp1 = Employee("Іван", 30000, 22, 10)
emp2 = Employee("Олена", 28000, 20, 5)

mgr1 = Manager("Андрій", 40000, 24, 15, 5)
mgr2 = Manager("Марія", 45000, 26, 20, 8)

employees.append(emp1)
employees.append(emp2)
employees.append(mgr1)
employees.append(mgr2)

print("\n РОЗРАХУНОК ЗАРПЛАТИ ТА БОНУСІВ ")
for emp in employees:
    print(f"\nІм'я: {emp.get_name()}")
    print("Зарплата за місяць:", round(emp.calculate_month_salary(), 2))
    print("Бонус:", round(emp.calculate_bonus(), 2))

    if isinstance(emp, Manager):
        print(emp.generate_report())