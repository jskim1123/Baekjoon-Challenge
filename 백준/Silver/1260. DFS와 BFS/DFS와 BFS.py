### basic concepts : 재귀를 이용한 DFS, 반복문을 이용한 BFS

from sys import stdin, setrecursionlimit
from collections import deque

def dfs(node) :
    if visited[node] == 0 : ### 방문하지 않은 노드
        visited[node] = 1 ### 방문 처리 후 출력
        print(node, end = " ")
        
        for nextNode in graph[node] : ### 현재 노드와 인접한 노드들에 대해 재귀함수 호출
            dfs(nextNode)
            
def bfs() :
    while queue : ### queue가 빌 때까지 반복
        node = queue.popleft() ### queue에서 가장 앞의 것을 pop
        
        if visited[node] == 1 : ### 이미 방문한 노드라면, 아래를 실행하지 않음
            continue
        
        visited[node] = 1 ### 방문하지 않은 노드라면, 방문 처리 후 출력
        print(node, end = " ")
        
        for nextNode in graph[node] : ### 현재 노드와 인접한 노드들 중 방문하지 않은 노드들을 queue에 push
            if visited[nextNode] == 0 :
                queue.append(nextNode)
            
setrecursionlimit(100000)

N, M, V = map(int, stdin.readline().strip().split(" "))

graph = {node : [] for node in range (1, N + 1)}
visited = [0] * (N + 1)
queue = deque([V])

for _ in range (M) :
    node1, node2 = map(int, stdin.readline().strip().split(" "))
    
    graph[node1].append(node2)
    graph[node2].append(node1)
   
for key in graph.keys() :
    graph[key].sort() ### 노드 번호가 작은 것부터 방문하기 위한 정렬
    
dfs(V) ### 깊이 우선 탐색

visited = [0] * (N + 1) ### visited 리스트 초기화

print("")

bfs() ### 너비 우선 탐색