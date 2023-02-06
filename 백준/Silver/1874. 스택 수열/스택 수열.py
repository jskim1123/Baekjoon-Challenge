import sys

stack = []
intList = []
operationStr = "" ### 연산 순서를 저장할 문자열

def push (stack : list, number : int) :
    
    global operationStr
    
    stack.append(number)
    operationStr += "+"
    
def pop (stack : list) :
    
    global operationStr
    
    stack.pop()
    operationStr += "-"
    
intNum = int(sys.stdin.readline())
intList = [num for num in range (1, intNum + 1)] ### 1부터 intNum까지의 정수를 요소로 갖는 리스트

try :
    for i in range (intNum) :
    
        num = int(sys.stdin.readline())
    
        if len(intList) == intNum : ### 수열의 첫번째 숫자
            for j in range (1, num + 1, 1) :
                push(stack, intList.pop(0))
            
        elif len(stack) == 0 or stack[-1] < num :
            for j in range (intList[0], num + 1, 1) :
                push(stack, intList.pop(0))
            
        elif stack[-1] > num :
            for j in range (stack[-1], num + 1, -1) :
                pop(stack)
                
        pop(stack)

except :
    print("NO")
    
else :
    for oper in operationStr:
        print(oper)