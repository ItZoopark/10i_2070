h = int(input("h= "))

for i in range(h): # i = [0..h]
    for j in range(h-i):
        print('', end=' ')
    for k in range(2*i+1):
        print('*', end='')
    print()