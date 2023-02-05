import sys

num = int(sys.stdin.readline())
isConstructor = False

for i in range (1, num, 1) :
    if (i + sum(map(int, str(i))) == num) :
        isConstructor = True
        break
        
if (isConstructor) :
    print(i)
    
else :
    print("0")