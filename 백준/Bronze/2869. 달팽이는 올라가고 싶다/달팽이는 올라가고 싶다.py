import sys
import math

### 올라가는 높이, 떨어지는 높이, 나무 막대기의 길이
upHeight, downHeight, stickHeight = map(int, sys.stdin.readline().split())

stickHeight -= upHeight
day = math.ceil(stickHeight / (upHeight - downHeight)) + 1

print(day) 