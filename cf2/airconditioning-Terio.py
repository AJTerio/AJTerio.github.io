import sys, math

# function to find the minimum cost of running the air conditioners
def find_min_cost(n, m, cows, acs):
    # initialize a list to store the minimum cooling requirement for each stall
    stalls = [0] * 101
    
    # iterate through all the cows and update the cooling requirement for their stalls
    for i in range(n):
        for j in range(cows[i][0], cows[i][1]+1):
            stalls[j] = max(stalls[j], cows[i][2])
    
    # initialize the minimum cost to a very large value
    min_cost = float('inf')
    
    # iterate through all possible combinations of air conditioners
    for i in range(2**m):
        # initialize a list to store the cooling effect of each air conditioner
        cooling = [0] * 101
        
        # iterate through all the air conditioners and update their cooling effect
        for j in range(m):
            if (i >> j) & 1:
                for k in range(acs[j][0], acs[j][1]+1):
                    cooling[k] += acs[j][2]
        
        # check if the cooling effect is enough to meet the cooling requirement of each stall
        if all(cooling[k] >= stalls[k] for k in range(1, 101)):
            # calculate the total cost of running the selected air conditioners
            cost = sum(acs[j][3] for j in range(m) if (i >> j) & 1)
            min_cost = min(min_cost, cost)
    
    # return the minimum cost
    return min_cost

# read input values
n, m = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(n)]
acs = [tuple(map(int, input().split())) for _ in range(m)]

# call the function to find the minimum cost
min_cost = find_min_cost(n, m, cows, acs)

# print the minimum cost
print(min_cost)