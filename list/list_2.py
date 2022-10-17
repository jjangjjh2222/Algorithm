L = [-3.2, 5.5, 4.1, 1.1, -1.3, 2.7, 0.5]
temp = L.copy()
temp.sort(reverse=True)
print(f'sorted={temp}')
for x in temp[:3]:
    while x in L:
        L.remove(x)
print(f'removed={L}')