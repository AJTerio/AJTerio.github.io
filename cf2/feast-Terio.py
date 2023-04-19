import sys, math

# opening file and assigning variables
file = open("feast.in", "r")
t, a, b = map(int, file.readline().split()) # t is maximum fullness, a is orange, b is lemon
file.close()

# Eating an orange increases her fullness by A
# and eating a lemon increases her fullness by B
# Bessie can drink water at most one time
# and drinking water decreases her fullness by 1/2
# help Besse find the maximum fullness she can achieve

fullness = [[0 for i in range(t+1)] for j in range(2)] # creating a 2d array to store fullness true or false
fullness[0][0] = 1 # starting fullness is 0

for i in range(2):
    for j in range(t+1): 
        if fullness[i][j] == 0:
            continue
        if j + a <= t:
            fullness[0][j+a] = 1
        if j + b <= t:
            fullness[0][j+b] = 1
        if i == 0:
            fullness[1][j//2] = 1

maxfullness = 0
for i in range(t+1):
    if fullness[0][i] == 1 or fullness[1][i] == 1:
        maxfullness = i

# output
file = open("feast.out", "w")
file.write(str(maxfullness))
file.close()