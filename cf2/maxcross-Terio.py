import sys, math

#opening file and assigning variables
file = open("maxcross.in", "r") #open file
n, k, b = [int(i) for i in file.readline().split()]
seen = [1] * (n + 1)
value = 0
for _ in range(b):
	seen[int(file.readline())] = 0
file.close()

seen.pop(0)

current = 0
for i in range(k):
	current += seen[i]

value = current
for i in range(k, n):
    current += seen[i] - seen[i - k]
    value = max(value, current)

answer = k - value

#output to file
file = open("maxcross.out", "w")
file.write(str(answer))
file.close()
