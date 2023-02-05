import sys

testCaseNum = int(sys.stdin.readline())

for i in range (testCaseNum) :
    
    floor = int(sys.stdin.readline()) ### k
    room = int(sys.stdin.readline()) ### n
    
    apartList = [[col + 1 for col in range (room)] for row in range (floor + 1)]
    
    for j in range (1, floor + 1, 1) :
        for k in range (1, room, 1) :
            apartList[j][k] = sum(apartList[j - 1][:k + 1])
            
    print(apartList[floor][room - 1])