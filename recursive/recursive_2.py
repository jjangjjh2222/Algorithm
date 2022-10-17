num=int(input())
bil=''
def binary(num):
    global bil
    while num>0 :
        bil += str(num%2)
        num = num//2
    print(bil[::-1])

binary(num)