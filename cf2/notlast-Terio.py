import sys, math

# opening file and assigning variables
file = open("notlast.in", "r") # open file
n = int(file.readline()) # assigning first line to N (number of milkings)
cows = {} # dictionary of the 7 cows and their milk
for i in range(0, n): # for loop to assign cows and their milk
    line = file.readline().split() # assigning line to a list of the two numbers
    if line[0] in cows: # if the cow is already in the dictionary
        cows[line[0]] += int(line[1]) # add the milk to the cow
    else: # if the cow is not in the dictionary
        cows[line[0]] = int(line[1]) # add the cow to the dictionary with the milk

minmilk = 1000000000 # minimum milk
# for loop to find the cow with the second least milk
for cow in cows:
    if cows[cow] < minmilk:
        minmilk = cows[cow]

secondminmilk = 1000000000 # second minimum milk
secondmincow = "" # cow with the second least milk
# for loop to find the cow with the second least milk
for cow in cows:
    if cows[cow] < secondminmilk and cows[cow] > minmilk:
        secondminmilk = cows[cow]
        secondmincow = cow

# case where there is only 1 cow
if len(cows) == 1:
    secondmincow = list(cows.keys())[0]

# output to file
out = open("notlast.out", "w")
if secondmincow == "":
    out.write("Tie")
else:
    out.write(secondmincow)
out.close()