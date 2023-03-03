from sys import stdin

num1 = int(stdin.readline())
num2 = int(stdin.readline())

units = num2 % 10 ### 일의 자리
tens = (num2 // 10) % 10 ### 십의 자리
hundreds = (num2 // 100) ### 백의 자리

thirdValue = num1 * units
fourthValue = num1 * tens
fifthValue = num1 * hundreds

print(thirdValue)
print(fourthValue)
print(fifthValue)
print(thirdValue + fourthValue * 10 + fifthValue * 100)