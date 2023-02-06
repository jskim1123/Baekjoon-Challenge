import sys

testCaseNum = int(sys.stdin.readline())

for testCase in range (testCaseNum) :
    
    printNum = 0
        
    documentNum, targetIdx = map(int, sys.stdin.readline().strip().split(" "))
    queue = list(map(int, sys.stdin.readline().split(" ")))
    
    while len(queue) > 0 :
        
        if (targetIdx == 0 and queue[0] == max(queue)) : ### 타겟이 첫번째에 있고, 중요도가 최대인 경우
            printNum += 1
            print(printNum)
            break
        
        elif (targetIdx == 0) : ### 타겟이 첫번째에 있지만, 중요도가 최대가 아닌 경우
            if (targetIdx == 0 and queue[0] != max(queue)) :
                queue.append(queue.pop(0))
                targetIdx = len(queue) - 1
            elif (queue[0] != max(queue)) :
                targetIdx -= 1
            else : 
                printNum += 1
                queue.pop(0)
                    
        else : ### 타겟이 첫번째에 있지 않은 경우
            if (queue[0] != max(queue)) : 
                queue.append(queue.pop(0))
            elif (queue[0] == max(queue)) :
                queue.pop(0)
                printNum += 1
                
            targetIdx -= 1