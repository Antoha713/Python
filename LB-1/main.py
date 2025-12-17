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
books = {}
while True:
    book_input = input("Введіть назву книги та автора, розділені комою (або 'stop' для завершення): ")
    if book_input.lower() == 'stop':
        break
    try:
        book, author = book_input.split(',', 1)  # Розділяємо введення на назву книги та автора
        books[book.strip()] = author.strip()  # Видаляємо зайві пробіли та зберігаємо дані
    except ValueError:
        print("Некоректний ввід, спробуйте ще раз.")
book_to_find = input("Введіть назву книги для пошуку її автора: ")
if book_to_find in books:
    print(f"Автор книги '{book_to_find}': {books[book_to_find]}")
else:
    print("Книга не знайдена в базі даних.")
