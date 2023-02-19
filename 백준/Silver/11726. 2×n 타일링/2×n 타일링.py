### basic concepts : 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수는, n을 1과 2의 합으로 나타내는 방법의 수와 동일함.
###                : n의 가짓수는 n-1의 가짓수 + n-2의 가짓수

from sys import stdin

### 숫자를 1, 2의 합으로 나타내는 방법의 수 리스트
numList = [1, 2] ### 1의 가짓수, 2의 가짓수

n = int(stdin.readline())

if (n == 1 or n == 2) :
    print(n % 10007)

else :
    for idx in range (len(numList), n, 1) :
        numList.append(numList[idx-1] + numList[idx-2])
        
    print(numList[-1] % 10007)