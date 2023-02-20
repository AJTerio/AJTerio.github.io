import sys, math

# opening file and assigning variables
file = open("square.in", "r") # open file
x1, y1, x2, y2 = map(int, file.readline().split(" ")) # assigning first line to x1, y1, x2, y2
x3, y3, x4, y4 = map(int, file.readline().split(" ")) # assigning second line to x3, y3, x4, y4
file.close() # close file

# find the length of the longest side and square it
answer1 = abs(x3-x2)**2
answer2 = abs(y3-y2)**2
answer3 = abs(x4-x1)**2
answer4 = abs(y4-y1)**2
answer5 = abs(y2-y1)**2
answer6 = abs(y4-y3)**2
answer7 = abs(x2-x1)**2
answer8 = abs(x4-x3)**2
answer = max(answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8)

# write output to file
out = open("square.out", "w")
out.write(str(answer))
out.close()