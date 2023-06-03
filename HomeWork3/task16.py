import random
n = int(input("Введите количество элементов: "))
lst = [random.randrange(10) for _ in range(n)]
print(lst)
x = int(input("Какое число нужно найти: "))
count = 0
for i in lst:
    if i == x:
        count += 1
print(f"Число {x} встречается: {count} раз.")