import random
n = int(input("Введите количество элементов: "))
lst = [random.randrange(100) for _ in range(n)]
print(lst)
x = int(input("Какой число нужно найти?: "))

lst2 = []
for i in lst:
    lst2.append(abs(i-x))
print(f"Самое близкое число: {lst[lst2.index(min(lst2))]}")