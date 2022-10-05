print('x y z')
for x in range(2): #[0,1]
    for y in range(2): #[0,1]
        for z in range(2): #[0,1]
            if ((x or y) <= (z == x)) == 0:
                print(x, y, z)

# xyz
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
