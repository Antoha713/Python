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

def find_book_author(books_dict):
    book_to_find = input("Назву книги для пошуку автор: ")
    if book_to_find in books_dict:
        print(f"Автор книги '{book_to_find}': {books_dict[book_to_find]}")
    else:
        print("Книга не знайдена в базі даних.")

def main():
    books = {}
    books = add_book(books)
    find_book_author(books)

def remove_book(books_dict):
    book_to_remove = input("Введіть назву книги для видалення: ")
    if book_to_remove in books_dict:
        del books_dict[book_to_remove]
        print(f"Книга '{book_to_remove}' успішно видалена.")
    else:
        print("Книга не знайдена в базі даних.")
    return books_dict



main()


