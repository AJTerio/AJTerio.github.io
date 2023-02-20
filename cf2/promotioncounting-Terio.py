import math, sys

# opening file and assigning variables
file = open("promote.in", "r")
b1, b2 = map(int, file.readline().split(" "))
s1, s2 = map(int, file.readline().split(" "))
g1, g2 = map(int, file.readline().split(" "))
p1, p2 = map(int, file.readline().split(" "))
file.close()
# calculate promotion count
btos = (s2 + g2 + p2) - (s1 + g1 + p1)
stog = (g2 + p2) - (g1 + p1)
gtop = p2 - p1
# write output to file
out = open("promote.out", "w")
out.write(str(btos) + "\n" + str(stog) + "\n" + str(gtop))
out.close()