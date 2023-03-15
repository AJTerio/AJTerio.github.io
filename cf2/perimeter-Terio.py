N, R = 0, 0
grid = [['.' for _ in range(1002)] for _ in range(1002)] # pad with .'s
region = [[0 for _ in range(1002)] for _ in range(1002)]
area = [0] * 1000000
perimeter = [0] * 1000000

def visit(i, j, r):
    """
    Helper function to mark all the connected cells as part of a region and update its area.
    """
    to_visit = [(i, j)]
    while to_visit:
        current = to_visit.pop()
        i, j = current
        if region[i][j] != 0 or grid[i][j] == '.': continue
        region[i][j] = r
        area[r] += 1
        to_visit.append((i-1, j))
        to_visit.append((i+1, j))
        to_visit.append((i, j-1))
        to_visit.append((i, j+1))

def find_perimeters():
    """
    Helper function to compute the perimeter of each region.
    """
    for i in range(1, N+1):
        for j in range(1, N+1):
            r = region[i][j]
            if r == 0: continue
            if region[i-1][j] == 0: perimeter[r] += 1
            if region[i+1][j] == 0: perimeter[r] += 1
            if region[i][j-1] == 0: perimeter[r] += 1
            if region[i][j+1] == 0: perimeter[r] += 1

# Main function starts here
with open('perimeter.in', 'r') as fin, open('perimeter.out', 'w') as fout:
    N = int(fin.readline().strip())
    for i in range(N+2): grid[0][i] = grid[N+1][i] = '.'
    for i in range(1, N+1):
        grid[i][0] = grid[i][N+1] = '.'
        line = fin.readline().strip()
        for j in range(1, N+1):
            grid[i][j] = line[j-1]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if grid[i][j] == '#' and region[i][j] == 0:
                visit(i, j, R+1)
                R += 1
                
    find_perimeters()
 
    best_a, best_p = 0, 0
    for i in range(1, R+1):
        if area[i] > best_a or (area[i] == best_a and perimeter[i] < best_p):
            best_a = area[i]
            best_p = perimeter[i]
 
    fout.write(str(best_a) + " " + str(best_p) + "\n")