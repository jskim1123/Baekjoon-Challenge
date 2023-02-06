import sys

intNum = int(sys.stdin.readline())
intList = [0 for i in range (10000)]

for i in range (intNum) :
    intList[int(sys.stdin.readline().strip()) - 1] += 1
    
for i in range (len(intList)):
    if (intList[i] != 0) :
        for j in range (intList[i]) :
            sys.stdout.write(str(i + 1) + "\n")