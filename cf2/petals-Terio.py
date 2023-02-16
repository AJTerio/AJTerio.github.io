import sys, math

# read in input
n = int(input()) # number of flowers
petals = list(map(int, input().split())) # number of petals on each flower

photos = 0 # number of photos taken
for i in range(n): # for loop to go through each petal // 0 - 4
    for j in range(i, n): # for loop to go through each petal after the current petal // 0 - 4
        totalpetals = 0 # total number of petals between the current petal and the next petal
        for k in range(i, j + 1): # for loop to go through each petal between the current petal and the next petal // 0 - 
            totalpetals += petals[k] # counting petals
        bool = False # boolean to check if the total number of petals is divisible by the number of flowers
        for k in range(i, j + 1): # for loop to go through each petal between the current petal and the next petal
            if petals[k] * (j-i+1) == totalpetals: # if the number of petals on the current petal times the number of flowers between the current petal and the next petal is equal to the total number of petals between the current petal and the next petal
                bool = True
        if(bool):
            photos += 1 # add one to the number of photos taken
# write output to file
print(photos)