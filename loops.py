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
n = int(input("n= "))
f = 1
