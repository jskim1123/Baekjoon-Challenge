### basic concepts : 연산의 개수는 타겟이 덱의 첫번째 위치에 오기 위해 rotate해야 하는 수와 동일함
###                : 타겟의 인덱스와 0의 차, N - 1과 타겟의 인덱스의 차 중 적은 쪽을 택해 rotate

import sys
from collections import deque

operationCount = 0

N, M = map(int, sys.stdin.readline().strip().split(" "))
targetList = list(map(int, sys.stdin.readline().strip().split(" ")))

queue = deque([num for num in range (1, N + 1)])

for num in targetList :
    
    targetIdx = queue.index(num)
        
    if (targetIdx <= len(queue) - targetIdx) : ### 반시계 방향으로 회전
        queue.rotate(-1 * targetIdx)
        operationCount += targetIdx
        
    elif (targetIdx > len(queue) - targetIdx): ### 시계 방향으로 회전
        queue.rotate((len(queue) - targetIdx))
        operationCount += (len(queue) - targetIdx)
        
    queue.popleft()
            
print(operationCount)  