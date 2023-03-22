# opening the file and reading in variables
with open("milkvisits.in") as read:
	farm_num, query_num = [int(i) for i in read.readline().split()] # number of farms, number of queries
	farms = read.readline() # type of farm at each farm
	neighbors = [[] for _ in range(farm_num)] # list of neighbors for each farm
	for f in range(farm_num - 1): # read in edges
		f1, f2 = [int(i) - 1 for i in read.readline().split()] # farms are 1-indexed
		neighbors[f1].append(f2) # add each edge to the neighbors list
		neighbors[f2].append(f1)

	queries = [] # list of queries
	for _ in range(query_num): # read in queries
		query = read.readline().split() # query[0] is the farm, query[1] is the type of farm
		query[0], query[1] = int(query[0]) - 1, int(query[1]) - 1 # farms are 1-indexed
		queries.append(query) # add query to list of queries
		
# Find connected components
component_num = 0 # number of connected components
component = [-1] * farm_num # component number of each farm

for start_farm in range(farm_num): # process each farm
    # Don't process a farm if it's been visited already
    if component[start_farm] != -1: 
        continue 

    edge = [start_farm] # list of farms to process
    curr_type = farms[start_farm] # type of farm at the current farm
    while edge: # process each farm at the current connected component
        curr_farm = edge.pop() # get the next farm to process
        # Assign the current component number to the farm
        component[curr_farm] = component_num
        for neighbor_farm in neighbors[curr_farm]:
            # Visit a neighbor if it's new & is of the same type
            if farms[neighbor_farm] == curr_type and component[neighbor_farm] == -1:
                edge.append(neighbor_farm) # add the neighbor to the list of farms to process

    # increment component_num once a connected component has been processed
    component_num += 1

# Process queries and output results
with open("milkvisits.out", "w") as written:
	for a, b, milk in queries: # a is the farm, b is the type of farm
		if component[a] == component[b]: # If a & b are in the same component, check if the milk type is the same as the one the farmer likes
			print(1 if farms[a] == milk else 0, end="", file=written)
		else:
			# Output 1 otherwise because both milk types will be visited
			print(1, end="", file=written)
	print(file=written)