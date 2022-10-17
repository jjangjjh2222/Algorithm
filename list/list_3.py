a = ['K', 'o', 'r', 'e', 'a']
buff = []

for x in a[:4]:
    buff.append(x)
for _ in range(3):
    b = buff.pop()
    print(b)

    
print(buff)


