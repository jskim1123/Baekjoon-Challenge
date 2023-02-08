import sys

cardDic = {} ### 상근이가 가지고 있는 카드를 key, 개수를 value로 갖는 딕셔너리

N = int(sys.stdin.readline()) ### 상근이가 가지고 있는 카드의 개수
cardList = list(map(int, sys.stdin.readline().strip().split(" ")))
M = int(sys.stdin.readline()) ### 구해야 할 카드의 수
targetList = list(map(int, sys.stdin.readline().strip().split(" ")))

### 상근이가 갖고 있는 카드의 리스트를 순회하며 각 카드의 개수를 딕셔너리에 저장
for card in cardList :
    if card in cardDic.keys() :
        cardDic[card] += 1
    else :
        cardDic[card] = 1
        
### 개수를 출력해야 할 카드의 리스트를 순회하며 카드에 적힌 수를 key로 이용해 딕셔너리를 참조
for card in targetList :
    if card in cardDic.keys() :
        print(cardDic[card], end = " ")
    else :
        print("0", end = " ")