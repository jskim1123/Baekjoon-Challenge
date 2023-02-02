starNum = int(input())

for i in range(starNum) :
    for j in range (starNum) :
        if (j <= i) :
            print("*", end = "")
    print("")