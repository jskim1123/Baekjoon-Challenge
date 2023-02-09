import sys 

N, K = map(int, sys.stdin.readline().strip().split(" "))

coinList = [] ### 동전의 액수를 저장하는 리스트
coinTotalNum = 0 ### K원을 만들기 위해 필요한 최소 동전의 개수

for _ in range (N) :
    
    coin = int(sys.stdin.readline())
    
    if (coin <= K) : ### 입력된 동전의 액수가 만들고자 하는 K원보다 클 경우에는 리스트에 저장하지 않음
        coinList.append(coin)
        
idx = len(coinList) - 1
        
while idx >= 0 : ### 액수가 큰 동전부터 작은 순서로 K원을 만들기 위해 필요한 동전 개수를 coinTotalNum 변수에 저장
    
    coinNum = K // coinList[idx]
    
    if coinNum >= 1 :
        coinTotalNum += coinNum
        K = (K % coinList[idx])
        
    idx -= 1
    
print(coinTotalNum)