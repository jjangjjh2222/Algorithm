num = int(input("인원 수를 입력하세요 : "))
no = []
rec = {}

for x in range(num):
    i = int(input())
    no.append(i)

for y in no:
    k = int(input())
    rec[y]=k
lank=sorted(rec.items(), key=lambda x: x[1])

for z in range(3):
    h=(lank[z][1]//3600)
    m=(lank[z][1]%3600)//60
    sec=(lank[z][1]%3600)%60
    print(lank[z][0],h,m,sec)
