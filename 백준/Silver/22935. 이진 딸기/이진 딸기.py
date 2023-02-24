from sys import stdin
from math import ceil

targetNum = 0

T = int(stdin.readline())

for _ in range (T) :
    
    N = int(stdin.readline())
    
    remaining = N % 14 ### 14로 나눈 나머지
    
    if (ceil((N - 1) / 14 + 1) % 2 == 0) :
        targetNum = bin(remaining if (remaining) >= 2 else remaining + 14)[2:].zfill(4)

    else :
        targetNum = bin(16 - remaining if (remaining) >= 2 else 2 - remaining)[2:].zfill(4)

    targetNum = targetNum.replace('0', 'V')
    targetNum = targetNum.replace('1', '딸기')
    
    print(targetNum)