from random import randint
n = int(input("Введите количество элементов в списке: "))
p = int(input("Введите сдвиг: "))
a = [randint(1, 100) for i in range(n)]
print(a)
for j in range(p):
    last = a[-1]
    for i in range(n-1, 0, -1): # [n-1...1]
        a[i] = a[i-1]
    a[0] = last
print(a)
