import sys, math

# opening file and assigning variables
file = open("cowqueue.in", "r") # open file
n = int(file.readline()) # assigning first line to N (number of cows in line)
times = [] # list of times cows arrive
durations = [] # list of durations cows are in line
for i in range(0, n): # for loop to assign times and durations
    line = file.readline().split() # assigning line to a list of the two numbers
    times.append(int(line[0])) # adding the first number to the list of times
    durations.append(int(line[1])) # adding the second number to the list of durations

# for loop to sort the times and durations
for i in range(0, n): # for loop to go through each cow
    for j in range(0, n-i-1): # for loop to go through each cow after the current cow
        if times[j] > times[j+1]: # if the current cow arrives after the next cow
            temp = times[j] # swap the times
            times[j] = times[j+1]
            times[j+1] = temp
            temp = durations[j] # swap the durations
            durations[j] = durations[j+1]
            durations[j+1] = temp

# for loop to find the time the last cow gets in the farm
time = 0 # time the last cow gets in the farm
for i in range(0, n): # for loop to go through each cow
    if time < times[i]: # if the current cow arrives after the last cow
        time = times[i] + durations[i] # the current cow gets in the farm at the time it arrives plus the time it takes to milk it
    else: # if the current cow arrives before the last cow
        time += durations[i] # the current cow gets in the farm at the time the last cow gets in the farm plus the time it takes to milk it

# output to file
out = open("cowqueue.out", "w")
out.write(str(time))
out.close()