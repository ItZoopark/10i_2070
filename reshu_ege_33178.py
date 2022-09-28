for s in range(1, 100):
    s1 = s
    n = 36

    while s1 < 2020:
        s1 = s1 * 2
        n = n + 3

    if n == 60:
        print(s)
        break
