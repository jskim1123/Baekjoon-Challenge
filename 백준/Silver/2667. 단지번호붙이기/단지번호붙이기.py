from sys import stdin
from sys import setrecursionlimit

def dfs(x, y) :
    
    houseNum = 0
    
    if x < 0 or x >= N or y < 0 or y >= N : ### 지도를 벗어나는 경우
        return 0
    
    if graph[x][y] == 1 : ### 집이 있는 곳
        graph[x][y] = 0 ### 방문 처리
        
        houseNum += 1
        
        ### 한 단지의 전체 집 개수
        return houseNum + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y+1) +  dfs(x, y-1)
        
    return 0

setrecursionlimit(100000)

graph = []
resultList = []

N = int(stdin.readline())

for _ in range (N) :
    graph.append(list(map(int, stdin.readline().strip())))
    
for i in range (N) :
    for j in range (N) :
            result = dfs(i, j)
            
            if result != 0 :
                resultList.append(result)
       
resultList.sort()
         
print(len(resultList))
print("\n".join(list(map(str, resultList))))