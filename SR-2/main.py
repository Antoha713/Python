from input import input_employees
from salary import calculate_all_salaries

def print_employees(names, index=0):
    if index == len(names):
        return
    print(names[index])
    print_employees(names, index + 1)



