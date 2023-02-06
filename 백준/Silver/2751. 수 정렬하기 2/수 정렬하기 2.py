import sys

intNum = int(sys.stdin.readline())
numList = []

for i in range (intNum) :
    numList.append(int(sys.stdin.readline()))
    
numList.sort()

for num in numList :
    print(num)