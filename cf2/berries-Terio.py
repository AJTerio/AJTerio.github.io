import sys, math

# opening the file
file = open("berries.in", "r")
n, k = map(int, file.readline().split()) # n = number of berry trees, k = number of baskets
berries = list(map(int, file.readline().split())) # list of berries in each tree
file.close()

ans = 0 
max_berry = max(berries) # max number of berries in a tree

for i in range(1, max_berry + 1): # i = number of berries in a basket
    mod = i
    full = sum(b // mod for b in berries) # number of baskets that are full
    leftover = [b % mod for b in berries] # number of berries left in each tree
    leftover.sort(reverse=True) # sort the list of leftover berries in descending order
    max_bessie_berry = (k // 2) * i # max number of berries Bessie can get
    if full >= k: # if the number of full baskets is greater than or equal to k
        ans = max(ans, max_bessie_berry) # update the answer
    elif full >= k // 2 and len(leftover) >= k - full: # if the number of full baskets is greater than or equal to k // 2 and the number of leftover berries is greater than or equal to k - full
        idx = (full - k // 2) * i + sum(leftover[:k - full]) # calculate the number of berries Bessie can get
        ans = max(ans, idx) # update the answer

# output the result
file = open("berries.out", "w")
file.write(str(ans) + "\n")
file.close()