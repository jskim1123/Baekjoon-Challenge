import sys

kingPosition, rockPosition, N = map(str, sys.stdin.readline().strip().split(" "))

### 킹과 돌의 x, y 좌표를 [1, 8] 범위의 정수로 설정해 변수에 저장
kingX = ord(kingPosition[0]) - 64
kingY = int(kingPosition[1])
rockX = ord(rockPosition[0]) - 64
rockY = int(rockPosition[1])

for _ in range (int(N)) :
    
    direction = sys.stdin.readline().strip()
    
    if (direction == "R" and kingX < 8) :
        if (rockX == kingX + 1 and rockY == kingY and rockX < 8) :
            kingX += 1
            rockX += 1
        elif (rockX != kingX + 1 or rockY != kingY) :
            kingX += 1
            
    elif (direction == "L" and kingX > 1) :
        if (rockX == kingX - 1 and rockY == kingY and rockX > 1) :
            kingX -= 1
            rockX -= 1
        elif (rockX != kingX - 1 or rockY != kingY) :
            kingX -= 1      

    elif (direction == "B" and kingY > 1) :
        if (rockX == kingX and rockY == kingY - 1 and rockY > 1) :
            kingY -= 1
            rockY -= 1
        elif (rockX != kingX or rockY != kingY - 1) :
            kingY -= 1
        
    elif (direction == "T" and kingY < 8) :
        if (rockX == kingX and rockY == kingY + 1 and rockY < 8) :
            kingY += 1
            rockY += 1
        elif (rockX != kingX or rockY != kingY + 1) :
            kingY += 1
            
    elif (direction == "RT" and kingX < 8 and kingY < 8) :
        if (rockX == kingX + 1 and rockY == kingY + 1 and rockX < 8 and rockY < 8) :
            kingX += 1
            kingY += 1
            rockX += 1
            rockY += 1
        elif (rockX != kingX + 1 or rockY != kingY + 1) :
            kingX += 1
            kingY += 1
            
    elif (direction == "LT" and kingX > 1 and kingY < 8) :
        if (rockX == kingX - 1 and rockY == kingY + 1 and rockX > 1 and rockY < 8) :
            kingX -= 1
            kingY += 1
            rockX -= 1
            rockY += 1
        elif (rockX != kingX - 1 or rockY != kingY + 1) :
            kingX -= 1
            kingY += 1

    elif (direction == "RB" and kingX < 8 and kingY > 1) :
        if (rockX == kingX + 1 and rockY == kingY - 1 and rockX < 8 and rockY > 1) :
            kingX += 1
            kingY -= 1
            rockX += 1
            rockY -= 1
        elif (rockX != kingX + 1 or rockY != kingY - 1) :
            kingX += 1
            kingY -= 1
            
    elif (direction == "LB" and kingX > 1 and kingY > 1) :
        if (rockX == kingX - 1 and rockY == kingY - 1 and rockX > 1 and rockY > 1) :
            kingX -= 1
            kingY -= 1
            rockX -= 1
            rockY -= 1
        elif (rockX != kingX - 1 or rockY != kingY - 1) :
            kingX -= 1
            kingY -= 1

print(chr(kingX + 64) + str(kingY))
print(chr(rockX + 64) + str(rockY))