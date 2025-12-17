def input_employees():
    employees = {}

    n = int(input("Скільки співробітників потрібно ввести? "))

    for i in range(n):
        print(f"\nСпівробітник {i + 1}")
        name = input("Ім'я: ")
        salary = float(input("Заробітна плата: "))
        days = int(input("Кількість відпрацьованих днів: "))

        employees[name] = {
            "salary": salary,
            "days": days
        }

    return employees
