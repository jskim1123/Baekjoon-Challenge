### basic concepts : 큐를 이용한 요세푸스 순열
###                : K - 1만큼 pop, push 반복 후, K번째에 pop 및 출력

import sys

N, K = map(int, sys.stdin.readline().strip().split(" "))
queue = [num for num in range (1, N + 1, 1)]

print("<", end = "")

while len(queue) > 0 :
    
    for i in range (K - 1) :
        queue.append(queue.pop(0))
        
    print(queue.pop(0), end = ", " if len(queue) >= 1 else "")
    
print(">", end = "")