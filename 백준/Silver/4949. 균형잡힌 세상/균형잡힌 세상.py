import sys

while True :
    
    string = input() ### 공백으로 시작하는 경우, 공백까지 입력받아 저장함
    
    if (string == '.') : ### 종료 조건
        break
    
    else :
        try :
            stack = []
            
            for char in string :
                
                if (char == "[" or char == "(") :
                    stack.append(char)
                elif ((char == "]" and stack[-1] == "[") or (char == ")" and stack[-1] == "(")) :
                    del stack[-1]
                elif (char == "]" or char == ")") :
                    num = 100 / 0
                else :
                    continue
                
        except :
            print("no")
        
        else :
            print("yes" if len(stack) == 0 else "no")