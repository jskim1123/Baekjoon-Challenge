import sys

dotNum = int(sys.stdin.readline()) ### 점의 개수
dotDic = {} ### x좌표를 key, y좌표의 리스트를 value로 갖는 딕셔너리

for i in range (dotNum) :
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    
    if x in dotDic.keys() :
        dotDic[x].append(y)
    else :
        dotDic[x] = [y]
        
for y in dotDic.values() :
    y.sort() ### y좌표 오름차순 정렬
    
dotDic = dict(sorted(dotDic.items())) ### x좌표 오름차순 정렬

for x, ys in dotDic.items() :
    for y in ys :
        print(x, y)