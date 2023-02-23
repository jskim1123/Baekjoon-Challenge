from sys import stdin

num = int(stdin.readline())
numList = list(map(int, stdin.readline().strip().split(" ")))

numList.sort()

print(numList[0] * numList[-1])