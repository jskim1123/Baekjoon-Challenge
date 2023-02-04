while True:
    word = input()
    
    if word == "0" :
        break
    else :
        wordLen = len(word)
        isPalindrome = True
        
        for i in range (int(wordLen / 2)) :
            if word[i] == word [wordLen - 1 - i] :
                continue
                
            else :
                isPalindrome = False
                break
                
        if isPalindrome :
            print("yes")
            
        else :
            print("no")