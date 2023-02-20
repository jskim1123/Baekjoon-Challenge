from sys import stdin

totalMul = 1

S, K = map(int, stdin.readline().strip().split(" "))

while K > 0 :
    totalMul *= (S // K)
    S = S - (S // K)
    K -= 1
    
print(totalMul)