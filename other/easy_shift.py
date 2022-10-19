from random import randint
n = int(input("Введите количество элементов в списке: "))
p = int(input("Введите сдвиг: "))
a = [randint(1, 100) for i in range(n)]
print(a)
first = a[p:]
second = a[:p]
full = first + second
print(first)
print(second)
print(full)