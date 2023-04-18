import sys, math

# opening file and assigning variables
n = int(input()) # number of phrases
phrases = [] # list of phrases
for i in range(n): # for loop to go through each phrase
    phrases.append(input().upper().split())
Zodiacs = [
	"OX",
	"TIGER",
	"RABBIT",
	"DRAGON",
	"SNAKE",
	"HORSE",
	"GOAT",
	"MONKEY",
	"ROOSTER",
	"DOG",
	"PIG",
	"RAT"
]
names = []
years = 0
pivot = Zodiacs.index("OX") # index of the Ox
# for loop to go through each phrase
for i in range(n):
    names.append(phrases[i][0])
    if(phrases[i][3] == "PREVIOUS"):
        multiplier = -1
        difference = Zodiacs.index(phrases[i][4])
    else:
        multiplier = 1
    

# output to file   
print(phrases)