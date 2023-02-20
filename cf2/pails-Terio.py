import sys, math

# read in file
file = open("pails.in", "r")
x, y, m = map(int, file.readline().split(" ")) # read in x, y, and m
file.close() # close file

# create a list of all possible combinations of x and y pails
maxmilk = 0 # max amount of milk that can fit in pail m
# for loop to find all possible combinations of x and y pails
for first in range(m + 1): # for loop to go through all x pails
    current = x * first
    if current > m: # if the current amount of milk is greater than the max milk m can accomodate
        break # break out of the for loop
    else:
        for second in range(m + 1): # for loop to go through all y pails
            current = x * first + y * second
            if current > m: # if the current amount of milk is greater than the max milk m can accomodate
                break # break out of the for loop
            else:
                maxmilk = max(maxmilk, current) # find the max amount of milk that can fit in pail m between the current value and maxmilk

# write output to file
out = open("pails.out", "w")
out.write(str(maxmilk))
out.close()