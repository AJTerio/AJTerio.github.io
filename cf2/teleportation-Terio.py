import math, sys

# opening file and splitting variables into a list
file = open("teleport.in", "r")
vars = file.readline()
nums = vars.split()
file.close()

# defining variables
a = int(nums[0])
b = int(nums[1])
x = int(nums[2])
y = int(nums[3])

# calculate minimum distance
answers = []
answers.append(abs(a - b))
answers.append(abs(a - x) + abs(b - y))
answers.append(abs(a - y) + abs(b - x))
answer = (min(answers))

# write output to file
out = open("teleport.out", "w")
out.write(str(answer))
out.close()

#====================================================== End of code ====================