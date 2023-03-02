import math, sys

#opening file and assigning variables
file = open("paintbarn.in", "r") #open file
n, k = [int(i) for i in file.readline().split()] #assigning first line to n and k (number of rectangles and optimal layers of paint)
width = 1000 #width is 1000
barn = [[0 for _ in range(width + 1)] for _ in range(width + 1)] #barn is a 1001 by 1001 array of 0s
#for loop to assign n number of rectangles to the barn
for _ in range(n):
	start_x, start_y, end_x, end_y = [int(i) for i in file.readline().split()]
	# Set up the prefix sums array with all the corners of the given rectangle
	barn[start_x][start_y] += 1
	barn[start_x][end_y] -= 1
	barn[end_x][start_y] -= 1
	barn[end_x][end_y] += 1
file.close()

#set the valid area to 0
valid_area = 0
#go through each x and y coordinate in the barn
for x in range(width + 1):
    for y in range(width):
        if x > 0: #if x is greater than 0
            barn[x][y] += barn[x - 1][y] #add the x - 1 and y coordinate to the x and y coordinate
        if y > 0: #if y is greater than 0
            barn[x][y] += barn[x][y - 1] #add the x and y - 1 coordinate to the x and y coordinate
        if x > 0 and y > 0: #if x and y are greater than 0
            barn[x][y] -= barn[x - 1][y - 1] #subtract the x - 1 and y - 1 coordinate from the x and y coordinate
        valid_area += barn[x][y] == k #add 1 to valid area if the x and y coordinate is equal to k

#output to file
file = open("paintbarn.out", "w")
file.write(str(valid_area))
file.close()