### basic concepts : 분수가 약분 가능할 때, 분자와 분모의 최대 공약수로 약분하면 기약분수가 된다.

import sys

### 최대 공약수를 구하는 유클리드 알고리즘
def gcm(num1 : int, num2 : int) :
    
    biggerNum = num1 if (num1 > num2) else num2
    smallerNum = num1 if (biggerNum != num1) else num2
    
    while smallerNum > 0 :
        
        rem = biggerNum % smallerNum
        biggerNum = smallerNum
        smallerNum = rem
        
    return biggerNum
        
num1, den1 = map(int, sys.stdin.readline().strip().split(" "))
num2, den2 = map(int, sys.stdin.readline().strip().split(" "))

totalNum = num1 * den2 + num2 * den1 ### 분수 합의 분자
totalDen = den1 * den2 ### 분수 합의 분모

gcmNum = gcm(totalNum, totalDen)

print(totalNum // gcmNum, totalDen // gcmNum)