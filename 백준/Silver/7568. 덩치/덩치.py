import sys

xyList = [] ### 몸무게, 키를 나타내는 양의 자연수 x, y의 튜플을 원소로 갖는 리스트, 범위는 [10, 200]
k = 0 ### 덩치가 더 큰 사람의 수 (단, 덩치는 키와 몸무게가 모두 클 때 "크다"고 판단)

N = int(sys.stdin.readline()) ### 전체 사람의 수, 범위는 [2, 50]

for i in range (N) :
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    xyList.append((x, y)) ### (몸무게, 키)의 형태로 리스트에 추가
    
for i in range (0, len(xyList)) :
    k = 0 ### 한 사람마다 초기화
    x, y = map(int, xyList[i]) ### x, y에 몸무게, 키 저장
    
    for j in range (0, len(xyList)) :
        if i == j : ### 자신과의 비교 생략
            continue
        else : 
            weight, height = map(int, xyList[j]) ### weight, height에 상대의 몸무게, 키 저장
            if (x < weight and y < height) :
                k += 1
    print(k + 1, end = " ")