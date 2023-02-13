import sys

M = int(sys.stdin.readline()) ### 연산의 수

setList = [0] * 20 ### 1 ~ 20의 존재 여부를 나타내는 리스트

for _ in range (M) :
    
    operationList  = sys.stdin.readline().strip().split(" ")
    operation = operationList[0]
    
    if (len(operationList) == 1) :
        if (operation == "all") : ### all 연산
            setList = [1] * 20
        else :
            setList = [0] * 20 ### empty 연산
            
    else :
        num = int(operationList[1])
        isIncluded = setList[num - 1]
        
        if (operation == "add" and isIncluded == 0) : ### add 연산
            setList[num - 1] = 1
        elif (operation == "remove" and isIncluded == 1) : ### remove 연산
            setList[num - 1] = 0
        elif (operation == "check") : ### check 연산
            print(isIncluded)
        elif (operation == "toggle") : ### toggle 연산
            if (isIncluded) : 
                setList[num - 1] = 0
            else :
                setList[num - 1] = 1