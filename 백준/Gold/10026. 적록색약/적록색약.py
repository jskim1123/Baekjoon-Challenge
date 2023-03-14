### basic concepts : 재귀를 이용한 DFS
###                : 이전 색깔을 인자로 보낸 뒤, 현재 색깔과 비교
###                : 적록색약이 아닌 사람이 봤을 때의 경우를 먼저 계산하므로, 이때 'R'을 'G'로 바꿔 적록색약인 경우에 바로 계산할 수 있도록 했다.
###                : 단, 재귀 호출 시 graph[x][y]를 인자로 보내므로, 색깔을 바꾸는 것은 재귀 호출 뒤에 이루어져야 한다.

from sys import stdin, setrecursionlimit

def dfs(x : int, y : int, previousColor : str, mode : str) :
    
    if x < 0 or x >= N or y < 0 or y >= N : ### 구역을 벗어나는 경우
        return False
    
    ### 적록색약이 아니면서, 방문한 적이 없고, 이전 색과 현재 색이 동일한 경우
    if (mode == 'normal' and visited[x][y] == 0 and previousColor == graph[x][y]) :
            
        visited[x][y] = 1 ### 방문 처리
        
        dfs(x-1, y, graph[x][y], 'normal')
        dfs(x+1, y, graph[x][y], 'normal')
        dfs(x, y-1, graph[x][y], 'normal')
        dfs(x, y+1, graph[x][y], 'normal')
        
        if (graph[x][y] == 'R') : ### 적록색약인 경우의 계산을 위해 'R'과 'G'의 색을 하나로 통일
            graph[x][y] = 'G'
        
        return True
    
    ### 적록색약이면서, 방문한 적이 없고, 이전 색과 현재 색이 모두 'B'이거나 모두 'B'가 아닌 경우
    if (mode == 'colorWeakness' and visited[x][y] == 0 and ('B' not in previousColor + graph[x][y] or 'BB' == previousColor + graph[x][y])) :
        
        visited[x][y] = 1 ### 방문 처리
        
        dfs(x-1, y, graph[x][y], 'colorWeakness')
        dfs(x+1, y, graph[x][y], 'colorWeakness')
        dfs(x, y-1, graph[x][y], 'colorWeakness')
        dfs(x, y+1, graph[x][y], 'colorWeakness')
        
        return True
    
    return False

setrecursionlimit(100000)

normalResult = 0 ### 적록색약이 아닌 사람이 봤을 때의 구역의 개수
colorWeaknessResult = 0 ### 적록색약인 사람이 봤을 때의 구역의 개수

N = int(stdin.readline())

graph = []
visited = [[0] * N for _ in range (N)]

for _ in range (N) :
    graph.append(list(map(str, stdin.readline().strip())))
   
### 적록색약이 아닌 경우 
for i in range (N) :
    for j in range (N) :
        if (dfs(i, j, graph[i][j], 'normal') == True) :
            normalResult += 1
            
visited = [[0] * N for _ in range (N)] ### 방문 리스트 초기화

### 적록색약인 경우
for i in range (N) :
    for j in range (N) :
        if (dfs(i, j, graph[i][j], 'colorWeakness') == True) :
            colorWeaknessResult += 1
            
print(normalResult, colorWeaknessResult)