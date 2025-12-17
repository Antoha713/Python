from input import input_employees
from salary import calculate_all_salaries

def print_employees(names, index=0):
    if index == len(names):
        return
    print(names[index])
    print_employees(names, index + 1)


employees = input_employees()

salaries = calculate_all_salaries(employees)

print("\n НАРАХОВАНА ЗАРПЛАТА ")
for name in salaries:
    print(name, ":", salaries[name])

print("\n СПИСОК СПІВРОБІТНИКІВ (рекурсія) ")
names_matrix = list(employees.keys())
print_employees(names_matrix)
