class Employee:
    def __init__(self, name, salary, worked_days, bonus_percent=0):
        # Захищені атрибути
        self._name = name
        self._salary = salary
        self._worked_days = worked_days
        self._bonus_percent = bonus_percent