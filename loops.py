# print(*range(20))
# print(*range(10, 20))
# print(*range(1, 22, 2))
# print(*range(29, 1, -1))

# for i in range(10):
#     for j in range(10):
#         print(f"i={i}, j={j}", end=' ')
#     print()

# Простые числа ---------------------
# n = int(input("n= "))
# for i in range(1, n):
#     isPrime = True
#     for j in range(2, i):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime == True:
#         print(i, end=' ')
# Факториал ----------------------------
# 5! = 5*4*3*2*1
# n = int(input("n= "))
# f = 1
# for i in range(n, 1, -1): #2..n
#     f = f * i
#     print(f"i={i}, f={f}")
# Число сочетаний --------
n = int(input("n= "))
k = int(input("k= "))

fn = 1
for i in range(n, 1, -1):
    fn = fn * i

fk = 1
for i in range(k, 1, -1):
    fk = fk * i

fnk = 1
for i in range(n-k, 1, -1):
    fnk = fnk * i

cnk = fn/(fk * fnk)
print(cnk)