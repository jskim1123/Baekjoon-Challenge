import sys

sugarWeight = int(sys.stdin.readline())

try:
    for num5Kg in range (sugarWeight // 5, -1, -1) :
        for num3Kg in range (sugarWeight // 3, -1, -1) :
            if (5 * num5Kg + 3 * num3Kg == sugarWeight) :
                error = 100 / 0

except :
    print(num5Kg + num3Kg)

else :
    print("-1")