L = [1,3,4,4,3,2,7,4,1,7,4]
temp = [4, 7]
for x in temp:
    while x in L:
        L.remove(x)

print(L)