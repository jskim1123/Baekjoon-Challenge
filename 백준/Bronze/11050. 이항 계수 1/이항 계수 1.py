import sys

N, K = map(int, sys.stdin.readline().split()) 

mul1 = 1
mul2 = 1

for i in range (K) :
    mul1 *= N
    mul2 *= K
    
    N -= 1
    K -= 1
    
print(mul1 // mul2)