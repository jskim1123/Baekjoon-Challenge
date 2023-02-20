from sys import stdin

tileList = [1, 1, 3]

while True :
    try :
        n = int(stdin.readline())
        
        while n >= len(tileList) : ### 리스트에 해당 숫자에 대한 경우의 수가 없다면, 연산을 통해 삽입함
            tileList.append(tileList[-1] + tileList[-2] * 2)
            
        print(tileList[n])
        
    except :
        break