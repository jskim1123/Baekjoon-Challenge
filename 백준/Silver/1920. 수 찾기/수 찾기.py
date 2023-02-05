### algorithms : 자료구조, 정렬, 이분 탐색

def binarySearch(targetNum, intList) :
    
    left = 0
    right = len(intList) - 1
    
    while left <= right :
        
        mid = (left + right) // 2
        
        if targetNum < intList[mid] : 
            right = mid - 1
        elif targetNum > intList[mid] :
            left = mid + 1
        else : ### targetNum == intList[mid], 즉 target number 발견
            return 1
        
    return 0

intNum = int(input())
intList = list(map(int, input().split(" ")))

targetIntNum = int(input())
targetIntList = list(map(int, input().split(" ")))

intList.sort()

for num in targetIntList :
    print(binarySearch(num, intList))
