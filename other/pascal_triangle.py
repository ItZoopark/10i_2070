h = int(input("h= "))
for n in range(h+1):
    for k in range(n+1):
        fn = 1
        for i in range(n, 1, -1):
            fn = fn * i

        fk = 1
        for i in range(k, 1, -1):
            fk = fk * i

        fnk = 1
        for i in range(n - k, 1, -1):
            fnk = fnk * i

        cnk = fn // (fk * fnk)
        print(cnk, end=' ')
    print()