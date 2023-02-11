import sys

stack = [1] ### 1번 컴퓨터부터 시작

computerNum = int(sys.stdin.readline()) ### 컴퓨터의 수
computerPairNum = int(sys.stdin.readline()) ### 직접 연결된 컴퓨터 쌍의 수

visitedList = [0] * computerNum
computerPairDict = {computer : [] for computer in range (1, computerNum + 1)} ### 컴퓨터 : 연결된 컴퓨터 리스트

for _ in range (computerPairNum) :
    
    computerPair = list(map(int, sys.stdin.readline().strip().split(" ")))
    computerPairDict[computerPair[0]].append(computerPair[1])
    computerPairDict[computerPair[1]].append(computerPair[0])
    
while stack :
    
    currentComputer = stack.pop()
    
    if visitedList[currentComputer - 1] == 1 : ### 이미 방문한 컴퓨터는 방문하지 않음
        continue
    
    else :
        visitedList[currentComputer - 1] = 1
    
        while computerPairDict[currentComputer] :
            stack.append(computerPairDict[currentComputer].pop())

print(sum(visitedList[1 : ])) 