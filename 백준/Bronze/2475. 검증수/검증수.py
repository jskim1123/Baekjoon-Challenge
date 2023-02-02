numArr = list(map(int, input().split(" ")))
squareSum = 0

for num in numArr :
    squareSum += num**2
    
print(squareSum % 10)