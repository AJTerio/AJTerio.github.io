import sys, math

# opening file and assigning variables
file = open("billboard.in", "r") # open file
x1, y1, x2, y2 = map(int, file.readline().split(" ")) # assigning first line to x1, y1, x2, y2 (coords of lawn mower billboard)
x3, y3, x4, y4 = map(int, file.readline().split(" ")) # assigning second line to x3, y3, x4, y4 (coords of cow billboard)
file.close() # close file

# count how many corners of the billboard are covered 
corners = 0
if x3 <= x1 <= x4 and y3 <= y1 <= y4:
    corners += 1
if x3 <= x2 <= x4 and y3 <= y1 <= y4:
    corners += 1
if x3 <= x1 <= x4 and y3 <= y2 <= y4:
    corners += 1
if x3 <= x2 <= x4 and y3 <= y2 <= y4:
    corners += 1
# if less than two corners are covered, the area is the area of the lawn mower billboard
if corners < 2:
    area = (x2-x1)*(y2-y1)
# if all four corners are covered, the area is 0
elif corners == 4:
    area = 0
# if two corners are covered, the area is the area of the lawn mower billboard minus the area of the overlap
elif corners == 2 or corners == 3:
    xL = math.max(x1, x3)
    xR = math.min(x2, x4)
    yL = math.max(y1, y3)
    yR = math.min(y2, y4)
    area = ((x2-x1)*(y2-y1)-(xR-xL)*(yR-yL))

# output to file
out = open("billboard.out", "w")
out.write(str(area))
out.close()