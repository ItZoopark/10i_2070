p = 2
count = 0
a = 3_000_000
b = 10_000_000
mean = 0
for x in range(a, b + 1):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            break
    else:
        if p != 2:
            if x - p == 2:
                count += 1
                mean = (x + p) / 2
            p = x
        else:
            p = x

print(count, mean)
