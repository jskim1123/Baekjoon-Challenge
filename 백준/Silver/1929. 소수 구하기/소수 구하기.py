import sys, math

M, N = map(int, sys.stdin.readline().strip().split(" "))

numList = [1] * (N - M + 1) 

for i in range (2, int(math.sqrt(N)) + 1, 1) : ### 2부터 루트 N까지의 배수를 확인
        for j in range (2 * i, N + 1, i) : ### 자기 자신을 제외한 배수
            if (j >= M and numList[j - M] == 1) : ### IndexError를 피하기 위한 j >= M
                numList[j - M] = 0 ### 배수들을 0으로 설정
                
for num in numList :
    if (M != 1 and num == 1) :
        print(num * M)
    M += 1