from sys import stdin

T = int(stdin.readline())

for _ in range (T) :
    A, B = map(int, stdin.readline().strip().split(" "))
    
    print("Case #{}: {} + {} = {}".format(_ + 1, A, B, A + B))