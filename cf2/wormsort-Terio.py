# reading input
with open("wormsort.in", "r") as read:
    n, m = map(int, read.readline().split())
    cows = list(map(int, read.readline().split()))
    cows = [c-1 for c in cows]  # make the cows 0-indexed

    max_width = 0
    neighbors = [[] for _ in range(n)]
    for _ in range(m): # iterate through the wormholes
        a, b, w = map(int, read.readline().split()) # a is the first cow, b is the second cow, w is the width
        a -= 1
        b -= 1
        neighbors[a].append((b, w)) # add the second cow and width to the list of neighbors of the first cow
        neighbors[b].append((a, w)) # add the first cow and width to the list of neighbors of the second cow
        max_width = max(max_width, w) # update the maximum width

# binary search
low = 0
high = max_width + 1 
valid = -1 # if valid is still -1 at the end, then the cows are already sorted or cannot be sorted
while low <= high:
    mid = (low + high) // 2 # mid is half of the current range of possible widths
    component = [-1] * n # component[c] is the component that cow c is in
    curr_comp = 0 # current component number

    for c in range(n): # iterate through cows
        if component[c] != -1: # if cow c has already been assigned a component, continue
            continue
        frontier = [c] # frontier is the list of cows that have been visited but not yet assigned a component
        while frontier: # while there are still cows in the frontier
            curr_cow = frontier.pop() # pop the last cow in the frontier and assign it as the current cow
            component[curr_cow] = curr_comp # assign the current cow to the current component
            for i, w in neighbors[curr_cow]: # iterate through neighbors of the current cow
                if component[i] == -1 and w >= mid: # if the neighbor has not been assigned a component and the width is greater than or equal to mid
                    frontier.append(i) # add the neighbor to the frontier
        curr_comp += 1 # increment the current component number

    sortable = all(component[c] == component[cows[c]] for c in range(n)) # check if all cows are in the same component as their sorted positions

    if sortable: # if the cows are sortable, then the width is valid
        valid = mid # update valid as potential answer
        low = mid + 1 # increase the width from the low end
    else: # if the cows are not sortable, then the width is not valid
        high = mid - 1 # decrease the width from the high end

# writing output
with open("wormsort.out", "w") as write:
    write.write(str(-1 if valid == max_width + 1 else valid) + "\n")