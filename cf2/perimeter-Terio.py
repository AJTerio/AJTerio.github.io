N, R = 0, 0 #number of rows and columns, number of regions
grid = [['.' for i in range(1002)] for i in range(1002)] # pad with .'s
region = [[0 for i in range(1002)] for i in range(1002)] #region[i][j] is the region number of the cell at (i, j)
area = [0] * 1000000 #area[i] is the area of region i
perimeter = [0] * 1000000 #perimeter[i] is the perimeter of region i

#Helper function to mark all the connected cells as part of a region and update its area.
def visit(i, j, r): #i, j is the starting cell, r is the region number
    tovisit = [(i, j)] #list of cells to visit
    while tovisit: #while there are still cells to visit
        current = tovisit.pop() #get the next cell to visit
        i, j = current #unpack the coordinates
        if region[i][j] != 0 or grid[i][j] == '.': continue #if it's already been visited or it's a ., skip it
        region[i][j] = r #mark the cell as part of the region
        area[r] += 1 #update the area of the region
        tovisit.append((i-1, j)) #add the neighboring cells to the list of cells to visit
        tovisit.append((i+1, j)) #add the neighboring cells to the list of cells to visit
        tovisit.append((i, j-1)) #add the neighboring cells to the list of cells to visit
        tovisit.append((i, j+1)) #add the neighboring cells to the list of cells to visit

#Helper function to compute the perimeter of each region.
def findperimeters(): #compute the perimeter of each region
    for i in range(1, N+1): #for each cell
        for j in range(1, N+1): #for each cell
            r = region[i][j] #get the region number
            if r == 0: continue #if it's not part of a region, skip it
            if region[i-1][j] == 0: perimeter[r] += 1 #if the cell above it is not part of a region, add 1 to the perimeter
            if region[i+1][j] == 0: perimeter[r] += 1 #if the cell below it is not part of a region, add 1 to the perimeter
            if region[i][j-1] == 0: perimeter[r] += 1 #if the cell to the left of it is not part of a region, add 1 to the perimeter
            if region[i][j+1] == 0: perimeter[r] += 1 #if the cell to the right of it is not part of a region, add 1 to the perimeter

#Main function
#opening file and reading input
with open('perimeter.in', 'r') as fin, open('perimeter.out', 'w') as fout:
    N = int(fin.readline().strip()) #number of rows and columns
    for i in range(N+2): grid[0][i] = grid[N+1][i] = '.' #pad with .'s
    for i in range(1, N+1): #read in the grid
        grid[i][0] = grid[i][N+1] = '.' #pad with .'s
        line = fin.readline().strip() #read in the line
        for j in range(1, N+1):
            grid[i][j] = line[j-1] #read in the character
    
    for i in range(1, N+1): #find all the regions
        for j in range(1, N+1): #and compute their areas
            if grid[i][j] == '#' and region[i][j] == 0: #if it's a new region
                visit(i, j, R+1) #mark all the connected cells as part of the region
                R += 1 #increment the number of regions
                
    findperimeters() #call the helper function to compute the perimeter of each region
 
    besta, bestp = 0, 0 #find the region with the smallest perimeter
    for i in range(1, R+1): #and the largest area
        if area[i] > besta or (area[i] == besta and perimeter[i] < bestp): #if it's the best region so far
            besta = area[i] #update the best area and perimeter
            bestp = perimeter[i] #update the best area and perimeter
 
    fout.write(str(besta) + " " + str(bestp) + "\n") #write the output to the file