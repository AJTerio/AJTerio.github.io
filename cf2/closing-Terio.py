import sys, math

#opening file and reading in data
file = open("closing.in", "r") 
n, m = map(int, file.readline().split()) #assigning first line to n (number of cows)

#assign each line to a list of coordinates
adj, order = {}, [] #adjacency list and order of closing barns
for i in range(1, n+1): #for each barn
    adj[i] = [] #create an empty list for each barn

visited, closed = [False] * (n+1), [False] * (n+1) #visited and closed barns
nodes = 0 #number of nodes visited

for i in range(m): #for each line after the first line
	a, b = map(int, file.readline().split()) #assigning each line to a and b
	adj[a].append(b) #undirected graph
	adj[b].append(a) #undirected graph
        
for i in range(n): #for each barn
    order.append(int(file.readline())) #adding the order of closing barns to a list

file.close() #closing input file

def dfs(node): #depth first search
    global nodes #number of nodes visited
    if visited[node] or closed[node]: #if the node is closed or visited,
        return 
    
    #visit the node if it isnt closed or visited
    visited[node] = True #mark the node as visited
    nodes += 1 #increment the number of nodes visited

    for u in adj[node]: #for each neighbor of the node
        if not visited[u]: #if the neighbor isnt visited
            dfs(u) #visit the neighbor

dfs(1)

sys.stdout = open("closing.out", "w") #opening output to file for print statements

if nodes == n: #if all nodes are visited
    print("YES") #print yes
else: #if not all nodes are visited
    print("NO") #print no

for i in range(n-1): #for each barn
    visited = [False] * (n+1) #reset visited
    nodes = 0 #reset nodes
    closed[order[i]] = True #close the barn
    dfs(order[n-1]) #visit the last barn
    if nodes == n-i-1: #if all nodes are visited
        print("YES") #print yes
    else: #if not all nodes are visited
        print("NO") #print no