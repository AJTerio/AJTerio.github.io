import sys, math

# opening file and assigning variables
with open("billboard.in", "r") as f:
    x1, y1, x2, y2 = map(int, f.readline().split()) # coordinates of the first billboard
    x3, y3, x4, y4 = map(int, f.readline().split()) # coordinates of the second billboard

# count how many corners of the billboard are covered 
corners = 0
if x3 <= x1 <= x4 and y3 <= y1 <= y4: # if the bottom left corner is covered
    corners += 1 
if x3 <= x2 <= x4 and y3 <= y2 <= y4: # if the top right corner is covered
    corners += 1
if x3 <= x1 <= x4 and y3 <= y2 <= y4: # if the top left corner is covered
    corners += 1
if x3 <= x2 <= x4 and y3 <= y1 <= y4: # if the bottom right corner is covered
    corners += 1

# calculate the area based on the number of corners covered
if corners < 2: # if no corners are covered, the area is the same as the first billboard
    area = (x2 - x1) * (y2 - y1) 
elif corners == 4: # if all corners are covered, the area is 0
    area = 0
else: # if 2 corners are covered, the area is the first billboard minus the overlapping area
    xL = max(x1, x3) # find the coordinates of the overlapping area
    xR = min(x2, x4) 
    yL = max(y1, y3)
    yR = min(y2, y4)
    area = ((x2 - x1) * (y2 - y1)) - ((xR - xL) * (yR - yL)) # calculate the area

# output to file
with open("billboard.out", "w") as f:
    f.write(str(area))