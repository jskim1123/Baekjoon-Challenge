from sys import stdin
from collections import deque, Counter

greenLightCount = 0
yellowLightCount = 0

correctAnswerQueue = deque([])
guessAnswerQueue = deque([])

for _ in range (3) :
    correctAnswerQueue.extend(list(stdin.readline().strip()))
    
for _ in range (3) :
    guessAnswerQueue.extend(list(stdin.readline().strip()))

### 알파벳 등장 횟수 계산
correctAnswerCounter = dict(Counter(correctAnswerQueue))
guessAnswerCounter = dict(Counter(guessAnswerQueue))

### green light 개수 계산
for idx in range (9) :
    
    correctAnswer = correctAnswerQueue[idx]
    guessAnswer = guessAnswerQueue[idx]
    
    if (guessAnswer == correctAnswer) :
        greenLightCount += 1
        correctAnswerCounter[correctAnswer] -= 1
        guessAnswerCounter[guessAnswer] -= 1
        
### yellow light 개수 계산
for word in guessAnswerCounter.keys() :
    if word in correctAnswerCounter.keys() :
        yellowLightCount += min(guessAnswerCounter[word], correctAnswerCounter[word])
    
print(greenLightCount)
print(yellowLightCount)