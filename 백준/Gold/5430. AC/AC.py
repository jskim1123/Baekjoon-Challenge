from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range (T) :
    
    try :
        
        isReversed = 0 ### R이면 1, 아니면 (또는 RR) 0

        p = stdin.readline().strip()
        n = int(stdin.readline())
        numDeque = deque(stdin.readline().replace("[", "").replace("]", "").strip().split(","))   
        
        for idx in range (len(p)) :
            
            if p[idx] == "R" :
                isReversed = 1 - isReversed ### isReversed 토글
                
            elif n == 0 : ### 배열이 비어있고, D이면
                error = 100/0 ### except로 이동
                
            elif isReversed == 1 : ### D이고, 선행한 R 때문에 뒤집힌 상태라면
                numDeque.pop() ### 뒤에서 삭제
                
            else : ### D이고, 뒤집히지 않은 상태라면
                numDeque.popleft() ### 앞에서 삭제
                
    except :
        print("error")
    
    else :
        
        if isReversed == 1 :
            numDeque.reverse()
                           
        print("[" + ",".join(numDeque) + "]")