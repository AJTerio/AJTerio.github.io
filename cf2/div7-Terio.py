import sys, math

#opening file and assigning variables
file = open("div7.in", "r") #open file
n = int(file.readline()) #assigning first line to N (number of milkings)
#assign n number of cows to a list
cows = []
for i in range(n):
    cows.append(int(file.readline()))
file.close()

#output the number of cows in the largest consecutive group whose sums add to a multiple of 7. If no such group exists, output 0.
#find the largest consecutive group whose sums add to a multiple of 7
#make maxint the max int
maxint = sys.maxsize
first = [0, maxint, maxint, maxint, maxint, maxint, maxint]
last = [0, 0, 0, 0, 0, 0, 0]
currPrefix = 0
for i in range(n):
    currPrefix += cows[i]
    currPrefix %= 7
    first[currPrefix] = min(first[currPrefix], i)
    last[currPrefix] = i

group = 0
for i in range(7):
    if first[i] <= n:
        group = max(group, last[i] - first[i])

#output to file
file = open("div7.out", "w")
file.write(str(group))
file.close()