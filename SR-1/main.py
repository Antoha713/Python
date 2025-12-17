import math

# 1
pib = input("Ваші прізвище, ім'я, по батькові? ")
age = int(input("Скільки Вам років? "))
city = input("Де Ви живете? ")
study_place = input("Де Ви навчаєтесь? ")
group = input("Номер Вашої групи? ")
number = int(input("Який Ваш порядковий номер у списку групи? "))

questions = [
    "Як справи?",
    "Як Ви себе почуваєте?",
    "Коли будете вдома?",
    "Яку оцінку отримав на ЗНО по українській мові?",
    "Сьогодні сонячно?",
    "Коли нарешті карантин?",
    "Як звати Вашого друга?",
    "Ви думаєте вступати у магістратуру?",
    "Якого кольору Ваш зошит?",
    "Який Ваш настрій сьогодні?"
]

answers = []

for q in questions:
    ans = input(q + " ")
    answers.append(ans)

print("\n РЕЗУЛЬТАТ ")
print("Ваше ім'я:", pib)
print("Ваш вік:", age)
print("Ви живете в:", city)
print("Ви навчаєтесь в:", study_place)
print("Номер моєї групи -", group)
print("Мій порядковий номер у списку групи -", number)

for i in range(len(questions)):
    print(f"{questions[i]} {answers[i]}")


# 2
x = int(input("Введіть x: "))
t = 1

Z = (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t))) * math.exp(x)

print("Z =", round(Z, 2))

# 3
x = float(input("Введіть x: "))

if x >= 0:
    f = 0.5 - abs(x) ** 0.25
else:
    f = (math.sin(x ** 2) ** 2) / abs(x + 1)

print("f(x) =", round(f, 2))

# 4
a = int(input("Введіть перше ціле число: "))
b = int(input("Введіть друге ціле число: "))
c = int(input("Введіть третє ціле число: "))
N = int(input("Введіть N: "))

numbers = [a, b, c]

print("Числа, що належать інтервалу [1, N]:")
for num in numbers:
    if 1 <= num <= N:
        print(num)


# 5
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

print("Мінімальне число:", min(a, b, c))
print("Максимальне число:", max(a, b, c))
