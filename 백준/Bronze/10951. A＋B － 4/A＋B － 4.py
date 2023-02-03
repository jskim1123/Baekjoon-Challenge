while True :
    
    try:
        testCaseList = list(map(int, input().split(" ")))
        print(testCaseList[0] + testCaseList[1])
        
    except EOFError :
        break