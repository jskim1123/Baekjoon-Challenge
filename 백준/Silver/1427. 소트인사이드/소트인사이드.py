from sys import stdin

N = list(map(int, list(stdin.readline().strip())))

N.sort(reverse=True)

for num in N :
    print(num, end = "")