import sys, math

# opening file and assigning variables
file = open("speeding.in", "r") # open speeding.in file
n, m = map(int, file.readline().split(" ")) # assigning first line to n and m 
# lists of varying ranges n or m to fill later
roadsegments = list(range(n))
speedlimits = list(range(n))
bessiejourney = list(range(m))
speeds = list(range(m))
# for loop to assign segments of road and speed limits across those segments
for i in range(n):
    roadsegments[i], speedlimits[i] = map(int, file.readline().split(" "))
# for loop to assign segments of bessie's journey and her speed across those segments
for i in range(m):
    bessiejourney[i], speeds[i] = map(int, file.readline().split(" "))
file.close() # close file

# create two lists for the speed limits over certain segments and bessie's speed over certain segments
speedsegments = []
bessiesegments = []
# for loop to fill the lists with the speed limits and bessie's speed
for i in range(n):
    for j in range(roadsegments[i]):
        speedsegments.append(speedlimits[i])
for i in range(m):
    for j in range(bessiejourney[i]):
        bessiesegments.append(speeds[i])

# find the max speed difference between bessie's speed and the speed limit
maxspeed = 0 # amount of speed bessie went over the speed limit
for i in range(100): # over the 100 mile length of the road
    if bessiesegments[i] > speedsegments[i]: #if bessie went over the speed limit
        maxspeed = max(maxspeed, bessiesegments[i] - speedsegments[i]) # find the max speed difference

# write output to file
out = open("speeding.out", "w")
out.write(str(maxspeed))
out.close()