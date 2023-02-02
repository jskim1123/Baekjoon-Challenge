wordDic = {} 
maxNum = 0 
maxWord = " "
isOnly = False 

sentence = input()

for word in sentence : 
    if (word.islower) : 
        word = word.upper()
    
    if (word in wordDic.keys()) :
        wordDic[word] += 1
    
    else :
        wordDic[word] = 1
        
for word in wordDic.keys() :
    if (wordDic[word] > maxNum) :
        maxWord = word
        maxNum = wordDic[word]
        isOnly = True
        
    elif (wordDic[word] == maxNum) :
        isOnly = False
    
if (not(isOnly)) :
    print("?")

else :
    print(maxWord)