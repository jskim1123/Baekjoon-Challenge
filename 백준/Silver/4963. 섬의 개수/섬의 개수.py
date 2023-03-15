### basic concepts : 재귀를 이용한 DFS
###                : 노드의 방문 여부를 확인하는 visited 리스트를 두지 않고, graph의 1(땅)을 0(바다)로 바꾼다.

from sys import stdin, setrecursionlimit

setrecursionlimit(100000)

def dfs(x, y) :
    if x < 0 or x >= h or y < 0 or y >= w : ### 지도를 벗어나는 경우
        return False
    
    if graph[x][y] == 1: ### 땅인 경우
        graph[x][y] = 0 ### 바다로 바꿔 방문 처리
        
        for dx, dy in directionVector :
            
            ### 방향 벡터를 하나씩 꺼내 현재 좌표에 더하면서 재귀함수 호출
            nx = x + dx
            ny = y + dy
            
            dfs(nx, ny)
            
        return True
    
    return False
        
### 움직일 수 있는 모든 방향 벡터 (상하좌우 + 대각선 4개)
directionVector = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

while True :
    w, h = map(int, stdin.readline().strip().split(" "))
    
    if (w == 0 and h == 0) : ### 종료 조건
        break
    
    result = 0
    graph = []
    
    for _ in range (h) :
        graph.append(list(map(int, stdin.readline().strip().split(" "))))
    
    for i in range (h) :
        for j in range (w) :
            if (dfs(i, j) == True) :
                result += 1
                
    print(result)