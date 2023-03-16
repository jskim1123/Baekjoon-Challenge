from sys import stdin, setrecursionlimit

def dfs(x, y) :
    if x < 0 or x >= N  or y < 0 or y >= M : ### 화면을 벗어나는 경우
        return False
    
    if graph[x][y] >= T : ### 경계값보다 크거나 같은 경우
        graph[x][y] = 0 ### 0으로 만들어 방문 처리
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        
        return True
    
    return False

setrecursionlimit(10 ** 6)

result = 0
graph = []

N, M = map(int, stdin.readline().strip().split(" "))

for _ in range (N) :
    
    graphRowSum = []
    
    graphRow = list(map(int, stdin.readline().strip().split(" ")))
    
    ### 3개씩 더해 평균을 낸 뒤, graph에 저장
    for idx in range (0, len(graphRow), 3) :
        graphRowSum.append(sum(graphRow[idx : idx + 3]) / 3)
    
    graph.append(graphRowSum)
    
T = int(stdin.readline())   

for i in range (N) :
    for j in range (M) :
        if (dfs(i, j) == True) :
            result += 1
            
print(result)  