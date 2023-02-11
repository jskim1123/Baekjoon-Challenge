### basic concepts : 누적 합
###                : 리스트의 n번째 원소에 n - 1번째 원소까지의 합을 누적으로 저장
###                : i번째부터 j번째까지의 합은, j까지의 누적 합에서 i - 1번째까지의 누적 합의 차 (단, i == 1이면 j까지의 누적 합)

import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))
numList = list(map(int, sys.stdin.readline().strip().split(" ")))

for idx in range (1, N) :
    numList[idx] += numList[idx - 1]

for _ in range (M) :
    
    start, end = map(int, sys.stdin.readline().strip().split(" "))
    
    if start == 1 :
        print(numList[end - 1])
        
    else :
        print(numList[end - 1] - numList[start - 2])