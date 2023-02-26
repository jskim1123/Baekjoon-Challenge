from sys import stdin
import heapq ### 디폴트가 최소 힙

maxHeap = []

N = int(stdin.readline())

for _ in range (N) :
    x = int(stdin.readline())
    
    if (x) :
        heapq.heappush(maxHeap, -x)
        
    elif (x == 0 and len(maxHeap) > 0) :
        print(-1 * heapq.heappop(maxHeap))

        
    else :
        print("0")