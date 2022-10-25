def printStar(n):
    if n > 0:
        print('*' * n)
        printStar(n-1)

printStar(5)


def printStar2(n):
    for i in range(1, n+1):
        print("*" * i)

printStar2(5)

def printStar3(n):
    for i in range(n, 0, -1):
        print("*" * i)

printStar3(5)