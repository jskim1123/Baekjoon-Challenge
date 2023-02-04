### basic concepts : 단어의 글자 수와 단어들의 리스트를 키와 값으로 갖는 딕셔너리를 사용함.
###                : sort()를 이용한 사전 순서 정렬

wordNum = int(input())
wordDic = {}

for i in range (wordNum) :
    word = input()
    
    if len(word) in wordDic.keys() and not (word in wordDic[len(word)]) :
        wordDic[len(word)].append(word)
    
    elif len(word) in wordDic.keys() and word in wordDic[len(word)] :
        continue
        
    else :
        wordDic[len(word)] = [word]
    
    wordDic[len(word)].sort() ### 사전 순으로 단어 정렬
        
for i in range (1, 51, 1) : ### [문제 조건] 단어의 최대 길이는 50
    
    if i in wordDic.keys() :
        
        for word in wordDic[i] :
            print(word)