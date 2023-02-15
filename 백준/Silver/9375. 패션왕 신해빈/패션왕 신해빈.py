import sys
from math import prod

testCaseNum = int(sys.stdin.readline())

for i in range (testCaseNum) :
    
    n = int(sys.stdin.readline())  
    
    clothesDict = {} ### key = 의상의 종류 value = 의상의 개수
            
    for j in range (n) :
    
        clothesType = (sys.stdin.readline().strip().split(" "))[-1]
    
        if clothesType in clothesDict.keys() :
            clothesDict[clothesType] += 1
        else :
            clothesDict[clothesType] = 2 ### 최종 의상의 개수에 1씩 더해 곱해야 하므로, 처음부터 2로 설정함
        
    print(prod(clothesDict.values()) - 1) ### 아무 것도 입지 않은 경우의 수 1을 뺌