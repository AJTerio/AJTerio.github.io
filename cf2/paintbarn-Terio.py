import math, sys

#opening file and assigning variables
file = open("paintbarn.in", "r") #open file
n, k = [int(i) for i in file.readline().split()]
width = 1000
barn = [[0 for _ in range(width + 1)] for _ in range(width + 1)]
#for loop to assign 
for _ in range(n):
	start_x, start_y, end_x, end_y = [int(i) for i in file.readline().split()]
	# Set up the prefix sums array with all the corners of the given rectangle
	barn[start_x][start_y] += 1
	barn[start_x][end_y] -= 1
	barn[end_x][start_y] -= 1
	barn[end_x][end_y] += 1
file.close()

valid_area = 0

for x in range(width + 1):
    for y in range(width):
        if x > 0:
            barn[x][y] += barn[x - 1][y]
        if y > 0:
            barn[x][y] += barn[x][y - 1]
        if x > 0 and y > 0:
            barn[x][y] -= barn[x - 1][y - 1]
        valid_area += barn[x][y] == k

#output to file
file = open("paintbarn.out", "w")
file.write(str(valid_area))
file.close()