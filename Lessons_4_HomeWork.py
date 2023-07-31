"""
HomeWork 6
Дано список цілих чисел, в якому зустрічаються однакові значення. Напишіть логіку для друку цього списку після видалення всіх однакових значень.

Вхідні дані:

45 67 23 45 111 67 12 55
Вихідні дані:

45 67 23 111 12 55"""
print("\nHomeWork 6")

list_1 = [45, 67, 23, 45, 111, 67, 12, 55]
print("Вхідні дані:", list_1)
list_2 = [repdig for i, repdig in enumerate(list_1) if repdig not in list_1[:i]]
print("Вихідні дані:", list_2)

"""HomeWork 7
Напишіть програму, яка по даному числу n від 1 до 9 виводить на екран n пінгвінів. Зображення одного пінгвіна має розмір 5 × 9 символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець. Дозволяється вивести порожній стовпець після останнього пінгвіна. Для спрощення малювання скопіюйте пінгвіна з прикладу в середовище розробки.

Вхідні дані:

3
Вихідні дані:

    _~_       _~_       _~_
   (o o)     (o o)     (o o)
  /  V  \   /  V  \   /  V  \
 /(  _  )\ /(  _  )\ /(  _  )\
   ^^ ^^     ^^ ^^     ^^ ^^
"""

print("\nHomeWork 7")

n = int(input("Введіть кількість пенгвінів:\n"))
penguin = [
    "    _~_    ",
    "   (o o)   ",
    "  /  V  \  ",
    " /(  _  )\ ",
    "   ^^ ^^   "
]
for x_p in penguin:
    print(x_p * n)

"""HomeWork 8
Користувач вводить рядок,

Ваша задача — сформатувати строку в хештег.

Декілька правил:

жодних інших символів із набору string.punctuation бути не повинно, в тому числі і пробілів
довжини хештега повинен бути не більше 140 символів, якщо довжина хештега більше 140 символів - обрізати підсумковий рядок до 140 символів.
Кожне слово починається з великої літери.
перед хештегом додати знак "#"
Приклад:

'Python Community' -> #PythonCommunity
'i like python community!' -> #ILikePythonCommunity
'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes"""

import string
print("\nHomeWork 8")

input_1 = input("Введіть рядок:\n")
words = input_1.translate(str.maketrans(",", " ", string.punctuation)).split()
words = [word.capitalize() for word in words]
hashtag = "#" + "".join(words)
hashtag = hashtag[:140]
print(hashtag)

"""HomeWork 9
Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати. 
Користувач вводить число, а програма перевіряє його і, якщо користувач не вгадав, що повідомляє ви введене число більше чи менше від згенерованого. 
Після цього знову просить вгадати. І так, поки користувач не вгадає."""

import random
print("\nHomeWork 9")

x_number = random.randint(1, 10)
while True:
    try:
        guess = int(input("Вгадайте число від 1 до 10: "))
        if guess == x_number:
            print("Ви вгадали!")
            break
        elif guess < x_number:
            print("Ваше число менше за загадане.")
        else:
            print("Ваше число більше за загадане.")
    except ValueError:
        print("Введіть коректне ціле число від 1 до 10.")

"""HomeWork 10
Створити програму, що виводить на екран числа від 1 до 100 при цьому заміняючи:

числа, що діляться на 3, на рядок Fizz
числа, що діляться на 5, на рядок Buzz
числа, що діляться і на 3, і на 5, на рядок FizzBuzz
Приклад виводу:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzB"""

print("\nHomeWork 9")
output = ""
count = 0
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        output += "FizzBuzz "
    elif num % 3 == 0:
        output += "Fizz "
    elif num % 5 == 0:
        output += "Buzz "
    else:
        output += str(num) + " "
    count += 1
    if count == 25:
        output += "\n"
        count = 0
print(output)