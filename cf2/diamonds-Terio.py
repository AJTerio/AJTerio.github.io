import sys, math

# read in file
file = open("diamond.in", "r")
n, k = map(int, file.readline().split(" ")) # read in n and k
diamonds = [] # list of diamonds
for i in range(n): # for loop to go through each diamond
    diamonds.append(int(file.readline())) # add diamond to list
file.close() # close file

maxdiamonds = 0 # max number of diamonds that can be showcased
# for loop to look at and compare each diamond 
for i in range(n): # for loop to go through each diamond
    count = 0 # number of diamonds that can be showcased
    for j in range(n): # for loop to compare diamond at i to each other diamond
        if(diamonds[j] >= diamonds[i] and diamonds[j] <= diamonds[i] + k): # if the difference between the diamonds sizes is less than or equal to k
            count += 1 # add one to the number of diamonds that can be showcased
    maxdiamonds = max(maxdiamonds, count) # find the max number of diamonds that can be showcased between the current value and maxdiamonds

# write output to file
out = open("diamond.out", "w")
out.write(str(maxdiamonds))
out.close()