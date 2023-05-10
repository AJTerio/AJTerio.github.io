import sys
from collections import deque
# manually perform input and output
n = int(input())
order = []
for _ in range(n):
    order.append(int(input()))
# reading input from file
# file = open("dishes.in", "r")
# n = int(file.readline()) # number of dishes
# order = [] # order of dishes
# # add all dishes to order
# for _ in range(n): 
#     order.append(int(file.readline()))

# function to return true if dishes with indexes [0, x) can be washed
def washable(x):
    not_washed = deque() # plates that have not been washed
    # add all plates to not_washed
    for i in range(x): 
        not_washed.append(order[i]) 
    # sort not_washed
    not_washed = deque(sorted(not_washed)) 

    # soapy is a list of stacks of soapy plates
    soapy = deque()
    # add first plate to first stack
    for i in range(x): 
        plate = order[i] # current plate

        # now we use binary search to find the stack that the plate can be placed in
        # l is the index of the stack that the plate can be placed in, r is the index of the stack that the plate cannot be placed in
        l, r = -1, len(soapy) 
        # binary search
        while l < r - 1: 
            mid = (l + r) // 2 # mid is the index of the stack that we are currently checking
            if soapy[mid][-1] > plate: # if the top plate of the stack is greater than the current plate, then we can place the plate in the stack
                r = mid 
            else: # otherwise, we cannot place the plate in the stack
                l = mid

        # if the plate cannot be placed in any existing stack
        if r == len(soapy):
            # create new stack
            soapy.append([plate])
        else:
            # place plate in stack
            soapy[r].append(plate)

        # elsie time
        # while there are soapy plates and the top plate of the first stack is the same as the first plate in not_washed
        while soapy and soapy[0][-1] == not_washed[0]:
            # remove the top plate of the first stack and the first plate in not_washed
            soapy[0].pop()
            not_washed.popleft()
            # and if first stack is empty, remove it
            if not soapy[0]:
                soapy.popleft()

    # returns true if every plate is washed
    return not_washed == deque()

# binary search for the longest possible prefix
l, r = 0, n + 1 # l is the longest possible prefix, r is the shortest impossible prefix
# binary search
while l < r - 1: 
    mid = (l + r) // 2 # the length of the prefix that we are currently checking
    if washable(mid): # if the prefix is washable, then we can check longer prefixes
        l = mid # so we set l to mid
    # otherwise, we cannot check longer prefixes
    else:
        r = mid # so we set r to mid
    
print(l)
# writing output to file
# file = open("dishes.out", "w")
# file.write(str(l))
# file.close()