#1
user_input = input("Будь ласка, введіть список чисел, розділених комами: ")
numbers_list = [int(item) for item in user_input.split(',')]
numbers_list.sort()
n = len(numbers_list)
if n % 2 == 1:
    median = numbers_list[n // 2]
else:
    median = (numbers_list[n // 2 - 1] + numbers_list[n // 2]) / 2

print(f"Медіана: {median}")

#2
def add_book(books_dict):
    while True:
        book_input = input("Назва та автор(або 'stop'): ")
        if book_input.lower() == 'stop':
            break
        try:
            book, author = book_input.split(',', 1)
            books_dict[book.strip()] = author.strip()
        except ValueError:
            print("Некоректний ввід, спробуйте ще раз.")
    return books_dict
