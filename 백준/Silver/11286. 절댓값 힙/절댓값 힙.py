### basic concepts : heap에 push할 때, (절댓값 : 양수(1)/음수(-1))으로 push함.
###                  기본적으로 push할 때 값이 튜플인 경우 첫번째 요소로 우선순위를 결정한다고 돼있는데,
###                  첫번째 요소가 같을 경우에는 두번째 요소까지 고려하는 듯함.

from sys import stdin
import heapq ### 디폴트가 최소 힙

absValueHeap = []

N = int(stdin.readline())

for _ in range (N) :
    x = int(stdin.readline())
    
    if (x > 0) :
        heapq.heappush(absValueHeap, (x, 1))
        
    elif (x < 0) :
        heapq.heappush(absValueHeap, (-x, -1))
        
    elif (x == 0 and len(absValueHeap) > 0) :
        value = heapq.heappop(absValueHeap)
        print(value[0] * value[1])

    else :
        print("0")