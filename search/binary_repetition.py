def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key<A[middle]) :
            return binary_search(A, key, low, middle - 1)
        else :
            return binary_search(A, key, middle + 1, high)
    return high


key = int(input())
a = input().split(' ')
a = list(map(int, a))
N = len(a)

print(f' {binary_search(a, key, 0, N-1)}')