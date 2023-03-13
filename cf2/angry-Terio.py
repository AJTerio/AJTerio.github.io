import sys, math

#opening file and reading in variables
file = open("angry.in", "r") #open file
n, k = map(int, file.readline().split()) #assigning first line to n and k (number of hay bales, and number of cows)
#assign n lines of hay bales
bales = [] #empty list of bales
#for loop to assign bales to the list
for i in range(n):
    bales.append(int(file.readline()))
file.close()

#find the minimum value for r such that k amount of cows are able to take out all the bales
bales.sort()
l, r = 0, bales[-1] - bales[0]
#use binary search to find the minimum value for r
while(l < r): 
    mid = (l + r) // 2 #midpoint
    cows = 1  
    last = bales[0] 
    for i in range(1, n): #for loop to find the number of cows
        if bales[i] - last > 2 * mid: #if the distance between the bales is greater than 2 * r
            cows += 1 #add a cow 
            last = bales[i] #set the last bale to the current bale
    if cows <= k: #if the number of cows is less than or equal to k
        r = mid #set r to mid
    else: #if the number of cows is greater than k
        l = mid + 1 #set l to mid + 1

#output to file
file = open("angry.out", "w")
file.write(str(l))