# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.

# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

N = int(input("Введите число: "))
i = 1
while 2 ** i <= N:
    print(2 ** i)
    i += 1