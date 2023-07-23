# import this
"""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# import antigravity
# открылся этот адрес https://xkcd.com/353/

# import __hello__
# ничего

# from __future__ import braces
"""Traceback (most recent call last):
  File "C:\Python311\Lib\code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\codeop.py", line 73, in _maybe_compile
    return compiler(source, filename, symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<input>", line 1
SyntaxError: not a chancу"""

# З допомогою Python порахувати наступні вирази для a=1, b=5, c=4:

import datetime
from math import sqrt
# pip install num2words

months_dict = {
    1: "Січня",
    2: "Лютого",
    3: "Березня",
    4: "Квітня",
    5: "Травня",
    6: "Червня",
    7: "Липня",
    8: "Серпня",
    9: "Вересня",
    10: "Жовтня",
    11: "Листопада",
    12: "Грудня"
}

a = 1
b = 5
c = 4

result_x1 = (-b + sqrt(b**2 - (4*a*c)))/2*a
print("X1 = ", result_x1)
result_x2 = (-b - sqrt(b**2 - (4*a*c)))/2*a
print("X2 = ", result_x2)

# Написати програму, що за допомогою функції input() запитує ім'я користувача і потім виводить вітання на екран. Наприклад:
# >>> Введіть ваше ім'я:
# ... Дмитро
# >>> Привіт, Дмитро!

name = input("Введіть ваше ім'я: \n")
print(f"Привіт, {name}!")

# Написати програму, що за допомогою функції input() запитує кількість гривень і потім виводить еквіваленте число доларів США
# (курс довільний -- можна підгледіти на будь-яку дату у вашому банку або у НБУ). Наприклад:
# >>> Введіть кількість гривень:
# ... 74.63
# >>> Станом на 15 липня 2022 року це становить 2.0 Долари США

how_mach_UAN = float(input("Введіть кількість гривень: \n"))
exchange_US = float(38.6)
today = datetime.date.today()
day_in_words = str(today.day)
month_in_words = months_dict[today.month]
year_in_words = str(today.year)
formatted_date = f"{day_in_words} {month_in_words} {year_in_words} року"
exchange_result = round(how_mach_UAN/exchange_US, 2)
print(f"Станом На {formatted_date} це становить: {exchange_result} Долари США.")

""" Додаткові завдання за бажанням:

Завдання 5.
Написати програму, що перетворює значення рядкової змінної з формату snake_case в формат CapitalizedWords (a.k.a. Capitalized camelCase).
Значення змінної отримуйте з input(). Для простоти вважаємо,
що значення змінної завжди складається з 3-х слів. Наприклад: 'employee_first_name' -> 'EmployeeFirstName'.

Завдання 6.
Даний рядок вигляду 'Taras Shevchenko*1814-03-09*1861-03-10', тобто вказане ім'я, прізвище та дати народження та смерті.
Написати програму, що отримуючи такий рядок через input() виводить на екран окремими рядками ім'я та прізвище людини та її вік в роках.
Для простоти при розрахунку віку можете ігнорувати число місяця та місяць. Тобто для рядку 'Taras Shevchenko*1814-03-09*1861-03-10' програма має вивести:
Name: Taras Schevchenko
Age: 47 years

Завдання 7.
Написати програму, що вираховує суму усіх цифр трьохзначного числа введеного корисувачем через input(). Виконати програму в двох варіантах:
a) З використанням рядків
b) Без використання рядків (після input() одразу приведіть текст до int() та не переводьте в рядок назад, а працюйте з цим числом)"""

