import sys
from collections import Counter ### 최빈값 계산을 위한 Counter

intNum = int(sys.stdin.readline())
intList = []
modeList = [] ### 최빈값 (Mode) 리스트

for i in range (intNum) :
    intList.append(int(sys.stdin.readline()))
    
intList.sort()

### 산술평균
print(round(sum(intList) / intNum)) ### round(반올림할 값, 반올림할 소수점 자릿수 - 1), 2번째 인자를 생략할 경우 소수점 첫째 자리에서 반올림

### 중앙값
print(intList[(intNum - 1) // 2])

countDict = Counter(intList)
modeList = [num for num, cnt in countDict.most_common(intNum) if cnt == countDict.most_common(1)[0][1]]

### 최빈값
print(modeList[1] if len(modeList) > 1 else modeList[0])

### 범위
print(intList[-1] - intList[0])