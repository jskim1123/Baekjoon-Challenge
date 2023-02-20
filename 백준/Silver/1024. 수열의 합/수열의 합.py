from sys import stdin

N, L = map(int, stdin.readline().strip().split(" "))

try :
    while True :
        startNum = (2*N/L - L + 1) / 2 ### 수열의 초항, 항의 개수 * (초항 + 마지막 항) / 2 = N을 이용한 공식

        if L > 100 :
            error = 100/0
        
        elif (startNum >= 0 and startNum == int(startNum)) :
            break
    
        else :
            L += 1

except :
    print("-1")   
    
else :     
    for idx in range (L) :
        print(int(startNum) + idx, end = " ")