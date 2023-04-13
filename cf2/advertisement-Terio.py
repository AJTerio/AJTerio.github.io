import sys, math

# opening file and reading in variables
file = sys.stdin.readline  # open file
# assign n to the number of vertical boards 
n = int(file().strip())
# assign the next line to a list of the heights of each vertical board
heights = list(map(int, file().split()))
heights.append(0) # add a 0 to the end of the list to fix indexing errors

# want to attach a rectangular advertisement to the fence. What is the maximum area of such an advertisement?
maxarea = 0 # empty list of max areas
index = [-1] # empty list of indexes

for i in range(n+1): # loop through the boards
    while heights[i] < heights[index[-1]]: # while the current board is less than the previous board
        h = heights[index.pop()] # pop the previous board
        w = i - index[-1] - 1 # find the width of the current board
        maxarea = max(maxarea, h * w) # find the maximum area of the current board
    index.append(i) # add the current board to the list of indexes
    
# output to file
print(maxarea)