from typing import List, Tuple

# Read input
n = int(input()) # Number of cows
x, y = set(), set() # Set of x and y coordinates
cows = [] # List of cows coordinates
for _ in range(n): # For each cow
    cow_coord = tuple(map(int, input().split())) # Read the coordinates in tuple form
    assert cow_coord[0] not in x and cow_coord[1] not in y # Assert that the coordinates are unique
    x.add(cow_coord[0]) # Add the x coordinate to the set
    y.add(cow_coord[1]) # Add the y coordinate to the set
    cows.append(cow_coord) # Add the cow coordinates to the list

# Perform coordinate compression in order to reduce the size of the data set while maintaining the relative ordering of the elements
cows.sort()  # Sort cows by x-coordinate
reduced_x_coords = {cows[c][0]: c for c in range(n)} # Map each x-coordinate to its index in the sorted list
cows.sort(key=lambda c: c[1])  # Sort cows by y-coordinate
reduced_y_coords = {cows[c][1]: c for c in range(n)} # Map each y-coordinate to its index in the sorted list
cows = [(reduced_x_coords[cow[0]], reduced_y_coords[cow[1]]) for cow in cows] # Replace each coordinate with its reduced coordinate
cows.sort() # Sort cows by x-coordinate again

# Create prefix sums for the y-coordinates
# Define 2 empty 2D arrays of size n x n + 1
less_than_y = [[0] * (n + 1) for _ in range(n)] # less_than_y[i][j] = number of cows with y-coordinate less than i in the range [0, j)
greater_than_y = [[0] * (n + 1) for _ in range(n)] # greater_than_y[i][j] = number of cows with y-coordinate greater than i in the range [0, j)
for y in range(n): # For each cow
    curr_y = cows[y][1] # Get the y-coordinate of the cow
    for x in range(1, n + 1): # For each x-coordinate
        less_than_y[curr_y][x] = less_than_y[curr_y][x - 1] + (cows[x - 1][1] < curr_y) # Increment the number of cows with y-coordinate less than curr_y in the range [0, x)
        greater_than_y[curr_y][x] = greater_than_y[curr_y][x - 1] + (cows[x - 1][1] > curr_y) # Increment the number of cows with y-coordinate greater than curr_y in the range [0, x)

# Count the number of rectangles
total = 0 # Total number of rectangles
for c1 in range(n): # For each cow
    for c2 in range(c1 + 1, n): # For each other cow
        bottom_y = min(cows[c1][1], cows[c2][1]) # Get the bottom y-coordinate of the rectangle
        top_y = max(cows[c1][1], cows[c2][1]) # Get the top y-coordinate of the rectangle
        # Get the number of cows with y-coordinate less than bottom_y in the range [c1 + 1, c2] and the number of cows with y-coordinate greater than top_y in the range [c1 + 1, c2]
        bottom_box_count = 1 + less_than_y[bottom_y][c2 + 1] - less_than_y[bottom_y][c1] # Add 1 to account for the current cow
        top_box_count = 1 + greater_than_y[top_y][c2 + 1] - greater_than_y[top_y][c1] # Add 1 to account for the current cow
        total += bottom_box_count * top_box_count # Add the number of rectangles that can be formed with the current cow and the other cow

# Finally add the boxes that contain no cows or a single cow
total += n + 1

# Print output
print(total)