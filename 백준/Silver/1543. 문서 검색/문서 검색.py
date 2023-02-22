from sys import stdin

i = 0 ### 인덱스
count = 0 ### 타겟 단어의 등장 횟수

document = stdin.readline().strip()
targetWord = stdin.readline().strip()

while i < len(document) :
    
    if (targetWord == document[i : i + len(targetWord)]) :
        count += 1
        i += len(targetWord) ### 인덱스를 타겟 단어의 길이만큼 증가시킴
        
    else :
        i += 1
        
print(count)