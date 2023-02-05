### basic concepts : 유클리안 호제법을 이용한 최대공약수 구하기, 최대공약수로 두 수의 곱을 나눠 최소공배수 구하기

import sys

num1, num2 = map(int, sys.stdin.readline().split())

### 유클리안 호제법, 유클리드 알고리즘
def euclidean (biggerNum, smallerNum) :
    
    while True :
        
        remainder = biggerNum % smallerNum
        
        if remainder == 0 :
            return smallerNum
        
        biggerNum, smallerNum = smallerNum, remainder

### gcd : greatest common divisor, 최대공약수
gcd = euclidean(num1, num2) if num1 > num2 else euclidean(num2, num1)

### lcd : least common multiple, 최소공배수
lcm = (num1 * num2) // gcd

print(gcd)
print(lcm)