a = int(input("a= ")) # 0<a<1000000 3195

d1 = a % 10 # 5
a = a // 10 # 19
if a == 0:
    if d1 % 3 == 0:
        print("Делится на 3")
    else:
        print("Не делится на 3")
else:
    d2 = a % 10 # в2 = 9
    a = a // 10 # a = 1
    if a == 0:
        if (d1 + d2) % 3 == 0:
            print("Делится на 3")
        else:
            print("Не делится на 3")
    else:
        d3 = a % 10 # d3 = 1
        a = a // 10 # a = 3
        if a == 0:
            if (d1 + d2 + d3) % 3 == 0:
                print("Делится на 3")
            else:
                print("Не делится на 3")
        else:
            d4 = a % 10 # d4= 3
            a = a // 10 # 0
            if a == 0:
                if (d1 + d2 + d3 + d4) % 3 == 0:
                    print("Делится на 3")
                else:
                    print("Не делится на 3")
