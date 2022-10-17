def selection_sort(a, b):
    for i in range(0, len(a)-1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
        b[i], b[minimum] = b[minimum], b[i]

num = int(input("인원 수를 입력하세요 : "))
no = []
rec = []
for i in range(num):
    no.append(int(input()))
for a in range(num):
    rec.append(int(input()))

selection_sort(rec, no)

rec = rec[0:3]
no = no[0:3]

for z in range(3):
    h=(rec[z]//3600)
    m=(rec[z]%3600)//60
    sec=(rec[z]%3600)%60
    print(no[z],h,m,sec)
    
                