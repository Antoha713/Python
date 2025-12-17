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