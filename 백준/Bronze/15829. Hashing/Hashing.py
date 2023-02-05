import sys

strLen = int(sys.stdin.readline())
string = sys.stdin.readline().strip() ### 개행문자 제거해서 입력받기
hashValue = 0
i = 0

for char in string : 
    hashValue += (ord(char) - 96) * (31 ** i)
    i += 1
    
print(hashValue)