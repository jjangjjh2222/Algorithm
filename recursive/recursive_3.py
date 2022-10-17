n = int(input())
bil=''
def binary(n):
    global bil
    if n==0:
        bil+='0'
        return
    elif n==1:
        bil+='1'
        return
    else:
        bil+=str(n%2)
        return binary(n//2)

binary(n)
print(bil[::-1])