### basic concepts : N >= 6일때, P(N)은 P(N - 1) + P(N - 5)가 성립함

import sys

serialList = [1, 1, 1, 2, 2] ### 파도반 수열 리스트

T = int(sys.stdin.readline())

for _ in range (T) :
    
    N = int(sys.stdin.readline())
    
    if (N > len(serialList)) : ### 파도반 수열 리스트에 타겟 넘버가 존재하지 않는 경우
        while (N > len(serialList)) :
            serialList.append(serialList[-1] + serialList[-5]) ### N까지 추가함
            
    print(serialList[N - 1])