import sys, math

#opening file and assigning variables
file = open("pairup.in", "r") #open file
n = int(file.readline()) #assigning first line to N (number of cards each cow gets)
#assign n lines of x cow pairs to a list
pair = [] #empty list of cows
#for loop to assign cows and milkings to the list
for i in range(n):
    cows, milkings = map(int, file.readline().split())
    pair.append([milkings, cows])
file.close()

#find the minimum amount of time farmer john can milk pairs of cows
pair.sort()
l, r = 0, n -1
mintime = 0

#while loop to find the minimum amount of time farmer john can milk pairs of cows
while(l <= r):
    sub = min(pair[l][1], pair[r][1]) #find the minimum amount of milkings
    mintime = max(mintime, pair[l][0] + pair[r][0]) #find the maximum amount of time
    if l == r: #if the left and right are the same
        sub /= 2 #divide the minimum amount of milkings by 2
    pair[l][1] -= sub #subtract the minimum amount of milkings from the left
    pair[r][1] -= sub #subtract the minimum amount of milkings from the right
    if pair[l][1] == 0: #if the left has no more milkings
        l += 1 #add 1 to the left
    if pair[r][1] == 0: #if the right has no more milkings
        r -= 1 #subtract 1 from the right

#output to file
file = open("pairup.out", "w")
file.write(str(mintime))
file.close()