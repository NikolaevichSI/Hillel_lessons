"""
HomeWork 15
1) Написати лямбда-функцію, що перевірить, чи є число парним і викликати її.

2) Написати рекурсивну функцію для пошуку максимального елемента в списку,

# Приклад
numbers = [3, 8, 1, 6, 10, 5]
print(find_max(numbers))  #  10

3) Дано список кортежів, кожен з яких містить два значення: назва фільму (рядок) і рейтинг (дійсне число).
Напишіть функцію(ї),  що поверне найбільш і найменш популярні з списку.

Вхідні дані:

[('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]

Вихідні дані:

Most popular: Avengers: Endgame - 8.7
Less popular: Captain Marvel - 7.0"""

print("\nHomeWork 15\n")

#1)
check_num = lambda x: x % 2 == 0
num_1 = int(input("Введіть число: \n"))
if check_num(num_1):
    print(f"{num_1} - Парнє число.")
else:
    print(f"{num_1} - Не парнє число.")

#2)
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_num = find_max(lst[1:])
        return lst[0] if lst[0] > max_num else max_num
num_2 = [3, 8, 1, 6, 10, 5]
print("\nСписок:", num_2, "\nМаксимальний елемент у списку:",find_max(num_2))

#3)
def find_pop_film(films):
    max_r = max(films, key=lambda x: x[1])
    min_r = min(films, key=lambda x: x[1])
    return max_r, min_r

films = [('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]
max_r, min_r = find_pop_film(films)
print(f"\nМакс. рейтинг: {max_r[0]} - {max_r[1]}")
print(f"Мін. рейтинг: {min_r[0]} - {min_r[1]}")

"""Доп ДЗ
Напишіть програму, яка друкує наступний день для певної дати як у вихідних даних у форматі рррр-мм-дд. 
Напишіть окремі функції для обробки даних, які вводить користувач і використайте їх у програмі.
Вхідні дані:

31 8 2019
28 2 2020
Вихідні дані:

2019-9-1
2020-2-29"""

print("\nHomeWork 15.3/4\n")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_next_day(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        days_in_month[1] = 29
    if day < days_in_month[month - 1]:
        return year, month, day + 1
    if month < 12:
        return year, month + 1, 1
    return year + 1, 1, 1

def main():
    day_1 = int(input("Введіть день для першої дати: "))
    month_1 = int(input("Введіть місяць для першої дати: "))
    year_1 = int(input("Введіть рік для першої дати: "))

    day_2 = int(input("Введіть день для другої дати: "))
    month_2 = int(input("Введіть місяць для другої дати: "))
    year_2 = int(input("Введіть рік для другої дати: "))

    next_day_1 = get_next_day(year_1, month_1, day_1)
    next_day_2 = get_next_day(year_2, month_2, day_2)

    print(f"\nПерша дата: {year_1}-{month_1}-{day_1}")
    print(f"Наступний день для першої дати: {next_day_1[0]}-{next_day_1[1]}-{next_day_1[2]}")
    print(f"\nДруга дата: {year_2}-{month_2}-{day_2}")
    print(f"Наступний день для другої дати: {next_day_2[0]}-{next_day_2[1]}-{next_day_2[2]}")
if __name__ == "__main__":
    main()





