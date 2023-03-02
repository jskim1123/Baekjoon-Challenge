from sys import stdin

numDict = {num : 0 for num in range (1, 31)}

for _ in range (28) :
    numDict[int(stdin.readline())] = 1
    
for key, value in numDict.items() :
    if value == 0 :
        print(key)