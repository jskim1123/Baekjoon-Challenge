### basic concepts : 스택을 이용한 VPS 판별
###                : (을 만나면 push, )을 만나면 pop
###                : 문자열 순회 도중 스택의 길이가 0인데 pop을 시도하면 -> (의 개수보다 )의 개수가 많아 VPS가 아님
###                : 문자열 순회 종료 후 스택의 길이가 0이 아니면 -> (의 개수가 )의 개수보다 많아 VPS가 아님
###                : VPS일 조건 = 문자열 순회 도중에는 스택의 길이가 0 이상, 종료 후에는 0

import sys

testCaseNum = int(sys.stdin.readline())
stack = [] ### 리스트를 이용한 스택

### item을 스택의 마지막에 push
def push (item : str, stack : list) :
    stack.append(item)
    
### 스택의 마지막 item을 pop
def pop (stack : list) :
    del stack[-1]
    
### VPS 판별
def isVPS (stack : list) :
    return "YES" if len(stack) == 0 else "NO"
    
for i in range (testCaseNum) :
    parenthesisStr = sys.stdin.readline().strip()
    
    try :
        stack = []
        
        for char in parenthesisStr :
            if (char == "(") :
                push(char, stack)
            else :
                pop(stack)
    
    except IndexError : ### try문에서 IndexError가 발생했을 경우 실행되는 블록
        print("NO") ### IndexError가 발생했다는 것은, 스택에 요소가 없는데 pop을 시도했다는 뜻이므로, VPS가 아님
        
    else : ### try문에서 오류가 발생하지 않았을 경우 실행되는 블록
        print(isVPS(stack))