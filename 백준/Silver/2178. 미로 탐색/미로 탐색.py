### basic concepts : 반복문을 이용한 BFS
###                : 최소 경로 거리를 구하기 위해, 인접한 노드들을 push할 때 현재 칸의 값에 1을 더해 인접한 칸에 저장

from sys import stdin
from collections import deque

def bfs(x, y) :
    
    queue.append((x, y))
    
    while queue :
        
        x, y = queue.popleft()
    
        if x == N - 1 and y == M - 1 : ### 목적지에 도달하면 종료
            return graph[x][y]
                
        for dx, dy in directionVector :
            nx = x + dx
            ny = y + dy
            
            ### 조건에 맞는 인접한 칸들을 push
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1 ### 경로 거리를 구하기 위해 현재 칸보다 1 큰 수를 저장
                queue.append((nx, ny))
                
    return -1
                    
graph = []
queue = deque()
directionVector = [(-1, 0), (1, 0), (0, 1), (0, -1)]

N, M = map(int, stdin.readline().strip().split(" "))

for _ in range (N) :
    graph.append(list(map(int, list(stdin.readline().strip()))))
    
print(bfs(0, 0))