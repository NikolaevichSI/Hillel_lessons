"""HomeWork 11
Дано два словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа.
В першому словнику можуть зустрічатися ключі чи значення, які присутні в другому словнику, або навпаки.
Наприклад, вміст словників може бути наступний: a = {'x' : 1, 'y' : 2, 'z' : 3}, b = {'w' : 10, 'x' : 11, 'y' : 2}.
Надрукуйте спільні ключі для обох словників в одному рядку через пропуск.

Вихідні дані:

y x"""

print("\nHomeWork 11")

a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}
print(a, b)
com_keys = []
for key in a:
    if key in b:
        com_keys.append(key)
for key in b:
    if key in a and key not in com_keys:
        com_keys.append(key)

print("Спільні ключі:", " ".join(com_keys))

"""HomeWork 12
Напишіть програму, яка підраховує і роздруковує кількість появ кожного символу у введеному рядку.

Вхідні дані:

abcabcdfghj
Вихідні дані:

a, 2
b, 2
c, 2
d, 1
f, 1
g, 1
h, 1
j, 1"""

print("\nHomeWork 12")

vd_1 = ("abcabcdfghj")
print("Вхідні дані:", vd_1)
dict_1 = {}
for sym_1 in vd_1:
    if sym_1 in dict_1:
        dict_1[sym_1] += 1
    else:
        dict_1[sym_1] = 1
for sym_1, num in dict_1.items():
    print(f"{sym_1}, {num}")


"""HomeWork 13
Вводиться число n, за яким слідують n рядків тексту. Напишіть програму, яка друкує всі слова, 
що зустрічаються в тексті, по одному на рядок, і їхню кількість входжень у текст. 
Слова повинні бути відсортовані в порядку спадання відповідно до їх кількості, 
і всі слова при однаковому числі входжень у текст повинні бути надруковані в лексикографічному порядку. 
Вказівка. Після того, як ви створите словник усіх слів, вам захочеться впорядкувати його по частоті слова. 
Бажаного можна домогтися, якщо створити список, елементами якого будуть кортежі з двох елементів: частота 
зустрічальності слова і саме слово. Наприклад, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тоді стандартне сортування 
буде сортувати список кортежів, при цьому кортежі порівнюються по першому елементу, а якщо ці елементи рівні - то по другому.

9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
Вихідні дані:

damme 4
is 3
name 3
van 3
bond 2
claude 2
hi 2
my 2
james 1
jean 1
what 1
your 1"""

print("\nHomeWork 13")
# тут прям сильно Chat GPT помог

n = int(input("Введіть кількість рядків: \n"))
word_count = {}
for i in range(n):
    line = input(f"Введіть {i+1}-й з {n} рядків: \n")
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

for word, count in sorted_word_count:
    print(f"{word}: {count}")