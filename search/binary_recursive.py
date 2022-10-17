# 문제 : (이진탐색-재귀버전) 정렬되어 있는 정수 키(사전)와 탐색할 키 k를 입력받아, 사전에서
# k의 위치를 출력하는 프로그램을 작성하시오. 

# ◦ 구현 조건
# - 입력 받은 사전의 키 저장 (중복 키는 없다고 가정) - 이진탐색을 이용하여 탐색 키의 위치 찾기 – O(log n) 시간 필요
# - 재귀 버전으로 구현

# ◦ 출력
# - x ≤ k 를 만족하는 사전의 키 x 중 가장 큰 값의 위치(즉, 인덱스) 출력
# (위치는 0부터 시작한다고 가정하고, 위 조건을 만족하는 x가 없는 경우 –1 출력) 
# - 즉, 키 k가 존재하는 경우에는 k의 위치를 출력하면 되고, 그렇지 않은 경우 k보다 작으면서 가장 큰 수의 위치를 출력하면 된다. 


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

