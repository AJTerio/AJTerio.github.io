import sys, math

# opening file and assigning variables
file = open("teamwork.in", "r") #open file
n, k = map(int, file.readline().split()) #assigning first line to n and k (n lines of skill levels, k number of cows on a team)
# Since cows learn from each-other, the skill level of each cow on a team can be replaced by the skill level of the most-skilled cow on that team.
# The most-skilled cow on a team is the cow with the highest skill level on that team.
# The skill level of a team is the max skill level of all the cows on the team

# assign n lines of skill levels
cows = [] #empty list of skill levels
# for loop to assign skill levels to the list
for i in range(n):
    cows.append(int(file.readline()))
file.close()

# we want to iterate through cows and keep track of the best sum to that point
# then we cn use that information to determine optimal groupings
dp = [-1] * n 
dp[0] = cows[0]
for i in range(1, n):
    maxCow = cows[i]
    for j in range(1, k+1):
        if i-j+1 < 0:
            break
        maxCow = max(maxCow, cows[i-j+1])
        if i-j >= 0:
            dp[i] = max(dp[i], dp[i-j] + maxCow*j)
        else:
            dp[i] = max(dp[i], maxCow*j)

# output to file
file = open("teamwork.out", "w")
file.write(str(dp[-1]))
file.close()