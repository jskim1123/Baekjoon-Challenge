### basic concepts : 2xn 크기의 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수는, n을 1, 2, 2*(2x2 타일로 가정)의 합으로 나타내는 방법의 수와 동일함.
###                : n의 가짓수는 n-1의 가짓수 + (n-2의 가짓수) * 2
###                : 우선 n을 1과 2의 합으로 나타내고, 2가 포함된 각각의 경우에서 2 대신 2*를 대치 가능하므로 가짓수는 2배가 됨.

from sys import stdin

numList = [1, 3]

n = int(stdin.readline())

if (n == 1 or n == 2) :
    print(numList[n-1])

else :
    for idx in range (len(numList), n, 1) :
        numList.append(numList[idx-1] + 2 * (numList[idx-2]))
        
    print(numList[-1] % 10007)