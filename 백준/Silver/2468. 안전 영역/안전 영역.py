from sys import stdin, setrecursionlimit

def dfs(x, y, height) :
    if x < 0 or x >= N or y < 0 or y >= N :
        return False
    
    elif visited[x][y] == 0 and graph[x][y] > height :
        visited[x][y] = 1
        
        dfs(x-1, y, height)
        dfs(x+1, y, height) 
        dfs(x, y+1, height)
        dfs(x, y-1, height)
        
        return True
    
    return False

setrecursionlimit(100000)
graph = []
minHeight = 101
maxHeight = 1
maxArea = 0

N = int(stdin.readline())

for _ in range (N) :
    
    graphRow = list(map(int, stdin.readline().strip().split(" ")))
    graph.append(graphRow)
    
    if minHeight > min(graphRow) :
        minHeight = min(graphRow)
        
    if maxHeight < max(graphRow) :
        maxHeight = max(graphRow)
     
for height in range (minHeight - 1, maxHeight + 1) :
    
    result = 0
    visited = [[0] * N for _ in range (N)]

    for i in range (N) :
        for j in range (N) :
            if (dfs(i, j, height) == True) :
                result += 1
       
    if result > maxArea :
        maxArea = result
        
print(maxArea)