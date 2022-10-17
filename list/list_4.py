import os
import random as r
import time as t

palja = [0] * 40
vic = 0
for k in range(5):
    pos = r.randrange(40)   # pos는 8이 들어갈 인덱스
    palja[pos] = 8
    for m in range(40):
        print('%2d ' % m, end = '')   # 0부터 39까지 출력
    print('\n')
    for m in range(40):
        print(' %d ' % palja[m], end = '')  # palja에 있는 값 출력
    print('\n')
    t.sleep(2)

    
    user = int(input('8자 어디에? : '))
    if user == pos :
        vic = vic + 1
        print('\n%d번 맞췄음' % vic)
    else :
        print('\n틀렸음. 맞춘 횟수 = %d' % vic)
    palja[pos] = 0
input()