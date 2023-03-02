import sys, math

#opening file and assigning variables
file = open("div7.in", "r") #open file
n = int(file.readline()) #assigning first line to N (number of milkings)
#assign n number of cows to a list
cows = [] #empty list of cows
#for loop to assign n number of cows to the list
for i in range(n):
    cows.append(int(file.readline()))
file.close()

#output the number of cows in the largest consecutive group whose sums add to a multiple of 7. If no such group exists, output 0.
#find the largest consecutive group whose sums add to a multiple of 7
#make maxint the max int
maxint = sys.maxsize #maxint is the max int
first = [0, maxint, maxint, maxint, maxint, maxint, maxint] #filling first list with 0 and maxint
last = [0, 0, 0, 0, 0, 0, 0] #filling last list with 0
currPrefix = 0
#for loop to go through each cow in cows
for i in range(n):
    currPrefix += cows[i] #add the cow id numbers to the current prefix
    currPrefix %= 7 #mod the current prefix by 7
    first[currPrefix] = min(first[currPrefix], i) #adding the smaller of the two numbers to the i index of first list
    last[currPrefix] = i #adding i to the i index of last list

group = 0 #group is 0
for i in range(7): #for loop to go through each index of first list
    if first[i] <= n: #if the first index is less than or equal to n
        group = max(group, last[i] - first[i]) #group is the max of the group and the last index minus the first index

#output to file
file = open("div7.out", "w")
file.write(str(group))
file.close()