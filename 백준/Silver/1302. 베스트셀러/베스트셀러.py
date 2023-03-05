from sys import stdin

bookDict = dict() ### key = book name, value = sold count

N = int(stdin.readline())

for _ in range (N) :
    
    book = stdin.readline().strip()
    
    if book in bookDict.keys() :
        bookDict[book] += 1
    else :
        bookDict[book] = 1
 
### value를 기준으로 내림차순 정렬하되, value가 동일한 경우에는 key를 오름차순으로 정렬      
bookDict = sorted(bookDict.items(), key=lambda x: (-x[1], x[0]))

print(bookDict[0][0])