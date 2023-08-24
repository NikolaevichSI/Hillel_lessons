"""HomeWork 18

Зчитати файл month.txt і порахувати кількість слів у ньому,
cтворити новий файл month_reversed.txt і записати слова у зворотньому порядку. """

"""HomeWork 19

Реалізуйте генератор, який буде генерувати "решітку" заданого розміру N x N з символів "#".
наприклад  3*3:
###
###
### """

print("\nHomeWork 19")

def gen_grid(N):
    if N <= 0:
        return "Размер должен быть больше 0"
    grid = ""
    for _ in range(N):
        x = "#" * N
        grid += x + "\n"
    return grid

try:
    N = int(input("Введите размер решетки N:\n"))
    grid = gen_grid(N)
    print(grid)
except ValueError:
    print("Некорректный ввод, пожалуйста, введите целое число.")






