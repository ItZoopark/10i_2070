
for x in range(174457, 174505+1):
    list_del = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            list_del.append(i)
            list_del.append(x//i)
    if len(list_del) == 2:
        print(list_del)
