import sys, math

# opening file and assigning variables
file = open("whereami.in", "r") # open file
n = int(file.readline()) # assigning first line to N (number of houses)
s = file.readline() # assigning second line to houses (string of houses)

# for loop to find the smallest number of letters that can be used to identify each house
for k in range(1, n+1): # for loop to test each number of letters
    good = True # boolean to check if the number of letters is good
    for i in range(0, n-k+1): # for loop to test each substring
        for j in range(i+1, n-k+1): # for loop to test each substring
            if s[i:i+k] == s[j:j+k]: # if the two substrings are the same
                good = False # the number of letters is not good
    if good: # if the number of letters is good
        break # break out of the for loop so that k is the smallest number possible

# output to file
out = open("whereami.out", "w")
out.write(str(k))
out.close()