import random
n = int(input("Введите количество элементов массива: "))
min = int(input("Введите минимальный сегмент: "))
max = int(input("Введите максимальный сегмент: "))

lst = [random.randrange(30) for _ in range(n)]
print(lst)
for i in range(n):
    if min <= lst[i] <= max:
        print(i, end=" ")