### basic concepts : 재귀를 이용한 DFS

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(x, y) :
    
    if x < 0 or x >= N or y < 0 or y >= M : ### 배추밭을 벗어나는 경우
        return False
    
    if graph[x][y] == 1 : ### 배추가 있는 경우
        graph[x][y] = 0 ### 방문 표시
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        
        return True
    
    return False

T = int(stdin.readline())

for _ in range (T) :
    M, N, K = map(int, stdin.readline().strip().split(" "))
    
    totalNum = 0
    graph = [[0] * M for __ in range (N)]
    
    for ___ in range (K) :
        X, Y = map(int, stdin.readline().strip().split(" "))
        graph[Y][X] = 1
        
    for i in range (N) :
        for j in range (M) :
            if (dfs(i, j) == True) :
                totalNum += 1
                    
    print(totalNum)