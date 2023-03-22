from collections import deque
#opening file and reading in variables
file = open("shuffle.in", "r")
n = int(file.readline())
shuffle = [int(x) for x in file.readline().split()]
cows_after_shuffle = [0] * n 

#shuffle cows
#assuming that shuffle_order represents the positions the n cows will move to each shuffle
#so if shuffle_order[0] = 3, then cow 1 will move to position 3
#if one of these positions is ever not filled, then add 1 to that index of cows_after_shuffle
#runs shuffle once
for i in range(n):
    shuffle[i] -= 1 #adjust for 0 indexing
    cows_after_shuffle[shuffle[i]] += 1 #add 1 to index of cows_after_shuffle

#calculate answer using cows after shuffle
answer = n #answer is the number of cows in the correct position after one shuffle
no_cows = deque() #queue of positions that are not filled

#find no_cows positions after one shuffle
for i in range(n):
    if cows_after_shuffle[i] == 0: #if position is not filled
        no_cows.append(i) #add to queue
        answer -= 1 #subtract 1 from answer

#run shuffle until all cows are in a position
while len(no_cows) != 0:
    curr = no_cows.popleft() #get next position that is not filled 
    cows_after_shuffle[shuffle[curr]] -= 1 #subtract 1 from index of cows_after_shuffle
    if cows_after_shuffle[shuffle[curr]] == 0: #if position is not filled
        no_cows.append(shuffle[curr]) #add to queue
        answer -= 1 #subtract 1 from answer

#output to file
file = open("shuffle.out", "w")
file.write(str(answer))
file.close()