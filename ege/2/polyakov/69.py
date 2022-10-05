print('a b c')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (a and not c) or (not b and not c)
            if f == 1:
                print(a, b, c)