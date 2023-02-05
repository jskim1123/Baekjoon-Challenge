import sys

targetNum = int(sys.stdin.readline()) ### N번째 종말의 숫자에서, N에 해당하는 타겟 넘버
num = 665 
cnt = 0 ### N번째 종말의 숫자에서, N에 해당하는 수

while cnt < targetNum :

    num += 1

    if ("666" in str(num)) :
        cnt += 1   

print(num) 