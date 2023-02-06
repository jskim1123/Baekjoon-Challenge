import sys

num = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split(" ")))
primeNum = 0

### 1만 입력될 경우
if [1] == numList : 
    primeNum = 0

else :
    
    if 1 in numList : ### 1이 포함된 경우
        del numList[numList.index(1)]
        
    maxNum = max(numList)
    
    for i in range (2, maxNum, 1) :
    
        j = 2
    
        while i * j <= maxNum :
        
            if (i * j in numList) :
                del numList[numList.index(i * j)] ### 배수의 인덱스를 찾아 리스트에서 삭제
            
            j += 1
            
    primeNum = len(numList)
        
print(primeNum)