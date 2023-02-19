from sys import stdin

inclusionCount = 0 ### P(N)이 S에 포함되는 횟수

N = int(stdin.readline())
M = int(stdin.readline()) ### S의 길이
S = stdin.readline().strip()

PN = "I" + "OI" * N
PNLen = 2 * N + 1

for idx in range (0, M - PNLen + 1, 1) :
    
    if S[idx] == "O" :
        continue
        
    elif S[idx : idx + PNLen] == PN :
        inclusionCount += 1
        
print(inclusionCount)