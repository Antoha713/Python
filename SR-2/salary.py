def calculate_salary(salary, days):
    return (salary / 30) * days


def calculate_all_salaries(employees):
    result = {}

    for name in employees:
        salary = employees[name]["salary"]
        days = employees[name]["days"]
        result[name] = round(calculate_salary(salary, days), 2)

    return result
