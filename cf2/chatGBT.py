import sys, math

#opening file and reading in data
with open('moocast.in', 'r') as f:
    #read input values
    n = int(f.readline().strip())
    x = [0] * n
    y = [0] * n
    p = [0] * n
    for i in range(n):
        line = f.readline().strip().split()
        x[i], y[i], p[i] = map(int, line)

    #create a boolean array to store which cows can transmit to other cows
    canTransmit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            #calculate the square distance between cow i and cow j
            squareDist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            # If cow i can transmit to cow j, set the corresponding entry in the boolean array to True
            if squareDist <= p[i] ** 2:
                canTransmit[i][j] = True

    #depth-first search on each cow to determine how many cows it can transmit to
    ret = 1
    for i in range(n):
        canHear = [False] * n
        if not canHear[i]:
            canHear[i] = True
            count = 1
            stack = [i]
            while stack:
                curr = stack.pop()
                for j in range(n):
                    if canTransmit[curr][j] and not canHear[j]:
                        canHear[j] = True
                        stack.append(j)
                        count += 1
            ret = max(ret, count)

#write output to file
with open('moocast.out', 'w') as f:
    f.write(str(ret) + '\n')