### basic concepts : N을 1, 2, 3의 합으로 나타내는 방법의 수는 N-1, N-2, N-3에서의 경우의 수를 합한 것과 동일함

import sys

caseList = [1, 2, 4] ### 1, 2, 3의 경우의 수

for idx in range (3, 10) :
    caseList.append(caseList[idx - 1] + caseList[idx - 2] + caseList[idx - 3])
    
T = int(sys.stdin.readline())

for _ in range (T) :
    print(caseList[int(sys.stdin.readline()) - 1])
    