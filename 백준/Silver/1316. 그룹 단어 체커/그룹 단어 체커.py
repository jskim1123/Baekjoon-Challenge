from sys import stdin

groupWordCount = 0

N = int(stdin.readline())

for _ in range (N) :
    
    alphabetDict = dict()
    stack = []
    
    word = stdin.readline().strip()
    
    try :
        for alphabet in word :
            
            ### 연속된 경우
            if (len(stack) > 0 and stack[-1] == alphabet) :
                stack.append(alphabet)
                alphabetDict[alphabet] += 1
                
            ### 연속되지 않은 경우
            elif (alphabet in alphabetDict.keys()) :
                error = 100/0
              
            ### 처음 등장한 경우  
            else :
                stack.append(alphabet)
                alphabetDict[alphabet] = 1
                
    except :
        continue
    
    else :
        groupWordCount += 1
        
print(groupWordCount)