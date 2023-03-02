import sys, math

#opening file and assigning variables
file = open("maxcross.in", "r")
n, k, b = [int(i) for i in file.readline().split()] #assigning first line to n, k, and b (number of street lights, number of lights that must be on, and number of broken lights)
seen = [1] * (n + 1) #seen is a list of 1s with n + 1 elements
value = 0 #value is 0
#for loop to go through each broken light
for _ in range(b): 
	seen[int(file.readline())] = 0 #assign the broken light to 0
file.close()

seen.pop(0) #remove the first element of seen

current = 0 #current is 0
#for loop to go through each index of seen
for i in range(k): 
	current += seen[i] #add the index of seen to current

value = current #value is current
for i in range(k, n): #for loop to go through each index of seen
    current += seen[i] - seen[i - k] #add the index of seen to current and subtract the index of seen - k from current
    value = max(value, current) #value is the max of value and current
answer = k - value #answer is k - value

#output to file
file = open("maxcross.out", "w")
file.write(str(answer))
file.close()
