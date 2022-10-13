from random import randint
n = int(input("Введите количество элементов в списке: "))
p = int(input("Введите сдвиг: "))
a = [randint(1, 100) for i in range(n)]

print(a[p:] + a[:p])