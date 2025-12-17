user_input = input("Будь ласка, введіть список чисел, розділених комами: ")
numbers_list = [int(item) for item in user_input.split(',')]
numbers_list.sort()