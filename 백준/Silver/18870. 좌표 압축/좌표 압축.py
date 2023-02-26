### basic concepts : set을 이용해 중복을 제거하고 sorted를 이용해 정렬 후 인덱스를 출력한다.

from sys import stdin
from collections import deque

N = int(stdin.readline())
dotDeque = deque((map(int, stdin.readline().strip().split(" "))))

sortedDotDeque = sorted(set(dotDeque)) ### set으로 중복을 제거한 뒤, sorted로 오름차순 정렬함
sortedDotDict = {sortedDotDeque[idx] : idx for idx in range (len(sortedDotDeque))}

for dot in dotDeque :
    print(sortedDotDict[dot], end = " ")