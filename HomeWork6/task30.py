a1 = int(input("Введите первый элемент последовательности: "))
d = int(input("Введите разницу: "))
n = int(input("Введите количество элементов: "))
lst = [a1]
for i in range(2, n+1):
    ai = a1+(i-1)*d
    lst.append(ai)
print(*lst)