import sys

memberNum = int(sys.stdin.readline()) 
memberDic = {}

for i in range (memberNum) :
    memberInfo = sys.stdin.readline().strip().split(" ")
    age = int(memberInfo[0])
    name = memberInfo[1]
    
    if age in memberDic.keys() :
        memberDic[age].append(name)
    else :
        memberDic[age] = [name]
        
for age, names in dict(sorted(memberDic.items())).items() :    
    for name in names :
        print(age, name)