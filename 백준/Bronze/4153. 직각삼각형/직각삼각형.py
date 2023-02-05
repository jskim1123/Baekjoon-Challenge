import sys

while True:
    
    numList = list(map(int, sys.stdin.readline().split(" ")))
    
    if (numList == [0, 0, 0]) :
        break
        
    else :
        maxNum = numList.pop(numList.index(max(numList)))
        numList = [num**2 for num in numList]

        if (maxNum ** 2 == numList[0] + numList[1]) :
            print("right")
            
        else :
            print("wrong")