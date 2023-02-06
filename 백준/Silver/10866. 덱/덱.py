import sys

deque = []
instNum = int(sys.stdin.readline())

for i in range (instNum) :
    
    instruction = sys.stdin.readline().strip()
    
    if " " not in instruction : ### pop_front, pop_back, size, empty, front, back
        
        if (instruction == "pop_front") :
            print("-1" if len(deque) == 0 else deque.pop(0))
        elif (instruction == "pop_back") :
            print("-1" if len(deque) == 0 else deque.pop(-1))
        elif (instruction == "size") :
            print(len(deque))
        elif (instruction == "empty") :
            print("1" if len(deque) == 0 else "0")
        elif (instruction == "front") :
            print("-1" if len(deque) == 0 else deque[0])
        else : ### back
            print("-1" if len(deque) == 0 else deque[-1])
    
    else : ### push_front, push_back
        
        inst, item = map(str, instruction.split(" "))
        
        if "front" in inst : ### push_front
            deque.insert(0, int(item))
        else : ### push_back
            deque.append(int(item))