from sys import stdin
from math import factorial

N = int(stdin.readline())

factorialNum = str(factorial(N))

for idx in range (len(factorialNum)-1, -1, -1) :
    if (factorialNum[idx] != "0") :
        print(factorialNum[idx])
        break