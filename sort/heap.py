a = input().split(' ')
a = [0] + list(map(int, a))

def print_val(a):
    for i in range(1, len(a)):
        print(a[i], end = ' ')
    print()


def downheap(i, size):
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k
        


def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        downheap(i, hsize)


def heap_sort(a):
    N = len(a) - 1
    cnt = 1
    for i in range(N-1):
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1)
        N -= 1
        print('sept', end = "")
        print(cnt,  ' = ', a)
        cnt += 1
        
    

print('정렬 전 : ', end = '')
print_val(a)
create_heap(a)
print('최대 힙 : ', end = '')
print_val(a)
heap_sort(a)
print('정렬 후 : ', end = '')
print_val(a)






