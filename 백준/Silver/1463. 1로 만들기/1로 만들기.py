### basic concepts : 바로 직전 수의 연산 횟수 + 1과 (직전 수가 되기 위해 -1 연산 한 번 소비)
###                : 현재 수 / 3의 연산 횟수 + 1과 (나누기 3 연산 한 번 소비)
###                : 현재 수 / 2의 연산 횟수 + 1 (나누기 2 연산 한 번 소비) 중 최솟값을 선택

import sys

N = int(sys.stdin.readline())
    
numList = [0] * (N + 1) ### 연산 횟수 리스트 (인덱스 == 해당 숫자)
        
for targetNum in range (2, N + 1) :
             
    numList[targetNum] = numList[targetNum - 1] + 1 ### 타겟 넘버보다 1 작은 수의 연산 횟수 + 1(-1 연산)
        
    if (targetNum % 2 == 0) : ### 타겟 넘버가 2의 배수라면 2으로 나눈 수의 연산 횟수와 lastNumOperCnt 중 작은 값 선택
        numList[targetNum] = min(numList[targetNum], numList[targetNum // 2] + 1)
        
    if (targetNum % 3 == 0) : ### 타겟 넘버가 3의 배수라면 3으로 나눈 수의 연산 횟수와 lastNumOperCnt 중 작은 값 선택
        numList[targetNum] = min(numList[targetNum], numList[targetNum // 3] + 1)

print(numList[N])