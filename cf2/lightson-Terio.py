import sys
sys.setrecursionlimit(100000)  # Raise recursion limit as the default will error

# reading input
file = open("lightson.in", "r")
n, m = map(int, file.readline().split())
# empty grid full of 0s (visited rooms)
visited = [[0 for _ in range(n)] for _ in range(n)]
# one more for rooms that are lit up
lit = [[0 for _ in range(n)] for _ in range(n)]
litrooms = 1
# reading in switches
# make empty grid of switches
switches = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, file.readline().split())
    switches[x-1][y-1].append((a-1, b-1))

# function to check if a room is connected to the main component of lit rooms
def connected(x, y):
    # arrays of directions to dictate which rooms to check
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
	# Iterate through neighbors
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
		# Ignore neighbor if out of bounds
        if new_x < 0 or new_y < 0 or new_x > n - 1 or new_y > n - 1:
            continue
		# If a neighbor has been visited
        if visited[new_x][new_y]:
            return True 
	# If no neighbors have been visited
    return False 

# floodfill function
def floodfill(x, y):
    global litrooms
    # mark room as visited
    visited[x][y] = 1
    # iterate through switches
    for i in switches[x][y]:
        # if the room is not lit, light it
        if not lit[i[0]][i[1]]:
            lit[i[0]][i[1]] = 1
            litrooms += 1
            # if the room is connected to the main component of lit rooms, floodfill it
            if connected(i[0], i[1]): 
                floodfill(i[0], i[1])
    # arrays of directions to dictate which rooms to check
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # Iterate through neighbors
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        # Ignore neighbor if out of bounds
        if new_x < 0 or new_y < 0 or new_x > n - 1 or new_y > n - 1:
            continue
        # If a neighbor has been visited
        if visited[new_x][new_y]:
            continue
        # If a neighbor is lit
        if lit[new_x][new_y]:
            floodfill(new_x, new_y)

# Mark room (1, 1) as lit
lit[0][0] = 1

# floodfill from room (1, 1)
floodfill(0, 0)

# writing to file
file = open("lightson.out", "w")
file.write(str(litrooms))
file.close()