### basic concepts : 주어진 x, y, r를 이용해 만든 원에, 출발점과 도착점 중 단 하나만 포함되는 경우의 수
###                : 진입/이탈이 불가피한 경우는, 출발점 혹은 도착점이 행성계 (원) 내부에 존재할 때

import sys

T = int(sys.stdin.readline().strip()) ### 테스트 케이스 개수

for i in range (T) :
    
    count = 0 ### 진입/이탈 횟수
    
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split(" ")) ### 출발점, 도착점
    n = int(sys.stdin.readline().strip()) ### 행성계의 개수
    
    for j in range (n) :
        
        cx, cy, r = map(int, sys.stdin.readline().strip().split(" ")) ### 행성계의 중점, 반지름
        
        ### 출발점, 도착점이 같은 행성계에 속하는 경우
        if ((x1 - cx)**2 + (y1 - cy)**2 <= (r**2)) and ((x2 - cx)**2 + (y2 - cy)**2 <= (r**2)) :
            continue
        
        ### 출발점, 도착점 중 하나만 행성계에 속하는 경우
        elif ((x1 - cx)**2 + (y1 - cy) ** 2 <= (r ** 2)) or ((x2 - cx)**2 + (y2 - cy)**2 <= (r**2)) : ### 출발점이 행성계에 포함
            count += 1
            
    print(count)