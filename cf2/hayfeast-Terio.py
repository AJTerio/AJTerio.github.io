import sys, math

# opening file and reading in variables
file = open("hayfeast.in", "r")  # open file
n, m = map(int, file.readline().split())  # assigning first line to n and k (number of hay bales, and the minimum amount of flavor)

# assign n lines of hay bales
bales = []  # empty list of bales
# for loop to assign bales to the list
# first index is the amount of flavor, second index is the amount flavor
for i in range(n):
    bales.append(tuple(map(int, file.readline().split())))
file.close()

# find the minimum amount of spice in a single course meal that satifsies the minimum amount of flavor
# loop through the bales and find the group of bales that satisfy the minimum amount of flavor whilst having the minimum amount of spice
left = 0
right = 0
spices = [] # list of spices in the current group of bales

while left < n and right < n: # loop through the bales
    totalFlavor = 0 # total amount of flavor in the current group of bales
    for i in range(left, right + 1): # loop through the current group of bales
        totalFlavor = totalFlavor + bales[i][0] # add the flavor of the current bale to the total amount of flavor
    if totalFlavor < m: # if the total amount of flavor is less than the minimum amount of flavor
        right += 1 # add another bale to the group
    else: # if the total amount of flavor is greater than or equal to the minimum amount of flavor
        maxSpice = 0 # the maximum amount of spice in the current group of bales
        window = right - left + 1 # the number of bales in the current group of bales
        tempSpice = [] # list of the amount of spice in each bale in the current group of bales
        for i in range(left, right + 1): # loop through the current group of bales
            tempSpice.append(bales[i][1]) # add the amount of spice in the current bale to the list 
        maxSpice = max(tempSpice) # find the maximum amount of spice in the current group of bales
        spices.append(maxSpice) # add the maximum amount of spice in the current group of bales to the list of spices
        left += 1 # remove the first bale from the group
ans = min(spices) # find the minimum amount of spice in the list of spices

# output to file
file = open("hayfeast.out", "w")
file.write(str(ans))
file.close()