import sys, math

# opening file and assigning variables
file = open("blocks.in", "r") # open file
n = int(file.readline()) # read first line and parse to int
# create alphabet, answer, and word list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [0] * 26

words = []
# for loop to assign words to list
for i in range(n):
    words.append(file.readline().strip('\n').split(" "))
file.close() # close file

# for loop to loop through the amount of blocks
for i in range(n):
    firstword = words[i][0] # first word in block
    secondword = words[i][1] # second word in block
    freq1 = [0] * 26 # frequency of letters in first word
    freq2 = [0] * 26 # frequency of letters in second word
    # for loop to loop through the letters in the alphabet
    for j in range(26):
        for k in range(len(firstword)): # loop through letters in first word
            if firstword[k] == alphabet[j]: # if letter in alphabet is in that index of first word
                freq1[j] += 1 # add to frequency
        for k in range(len(secondword)): # loop through letters in second word
            if secondword[k] == alphabet[j]: # if letter in alphabet is in that index of second word
                freq2[j] += 1 # add to frequency
        if freq1[j] > freq2[j]: # if frequency of first word is greater than second word
            answer[j] += freq1[j] # add to answer
        else:
            answer[j] += freq2[j] # add to answer
    
# write output to file
output = "" # empty string to output since usaco doesn't like print
for i in range(26): # loop through letter count
    output += str(answer[i]) + "\n" # everything on a new line and parse to string
out = open("blocks.out", "w") # open file
out.write(output) # write output
out.close() # close file