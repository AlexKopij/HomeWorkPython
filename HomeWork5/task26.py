

def func(a, b):
    if b == 0:
        return 1
    return a * func(a, b-1)


print(func(int(input("Введите число: ")), int(input("Введите степень в которую нужно возвести число: "))))