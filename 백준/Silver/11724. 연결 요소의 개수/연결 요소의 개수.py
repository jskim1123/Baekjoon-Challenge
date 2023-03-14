### basic concepts : 재귀를 이용한 DFS

from sys import stdin

def dfs (node) :
    if visitedList[node] == 0 : ### 방문하지 않은 노드라면
        visitedList[node] = 1 ### 방문 처리
        for nextNode in graph[node] : ### 인접 노드들로 재귀 호출
            dfs(nextNode)
        return True
    return False

result = 0 ### 출력 결과

N, M = map(int, stdin.readline().strip().split(" "))

visitedList = [0] * (N + 1) ### 방문 여부 리스트

graph = [[] for _ in range (N + 1)] ### 인접 리스트

for _ in range (M) :
    
    node1, node2 = map(int, stdin.readline().strip().split(" "))
    
    graph[node1].append(node2)
    graph[node2].append(node1)
    
for idx in range (1, N + 1) :
    if (dfs(idx) == True) :
        result += 1  

print(result)