import sys, math

#opening file and reading in data
with open('moocast.in', 'r') as f:
    #read input values
    n = int(f.readline().strip()) #assigning first line to n (number of cows)
    x = [0] * n #x coordinates
    y = [0] * n #y coordinates
    p = [0] * n #power of each cow
    for i in range(n): #for each cow
        line = f.readline().strip().split() #assigning each line to a list of coordinates
        x[i], y[i], p[i] = map(int, line) #assigning each line to a list of coordinates

    #create a boolean array to store which cows can transmit to other cows
    canTransmit = [[False] * n for _ in range(n)] #can cow i transmit to cow j?
    for i in range(n): #for each cow
        for j in range(n): #for each other cow
            #calculate the square distance between cow i and cow j
            squareDist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 #distance between cow i and cow j
            # If cow i can transmit to cow j, set the corresponding entry in the boolean array to True
            if squareDist <= p[i] ** 2: #if cow i can transmit to cow j
                canTransmit[i][j] = True #set the corresponding entry in the boolean array to True

    #depth-first search on each cow to determine how many cows it can transmit to
    ret = 1 #maximum number of cows that can be reached
    for i in range(n): #for each cow
        canHear = [False] * n #can cow i hear cow j?
        if not canHear[i]: #if cow i cannot hear cow j
            canHear[i] = True #cow i can hear cow j
            count = 1 #number of cows that cow i can hear
            stack = [i] #stack of cows that cow i can hear
            while stack: #while the stack is not empty
                curr = stack.pop() #pop the last cow from the stack
                for j in range(n): #for each cow
                    if canTransmit[curr][j] and not canHear[j]: #if cow i can transmit to cow j and cow i cannot hear cow j
                        canHear[j] = True #cow i can hear cow j
                        stack.append(j) #add cow j to the stack
                        count += 1 #increment the number of cows that cow i can hear
            ret = max(ret, count) #update the maximum number of cows that can be reached

#write output to file
with open('moocast.out', 'w') as f:
    f.write(str(ret) + '\n')