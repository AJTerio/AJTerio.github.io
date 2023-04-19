import sys, math

# opening file and assigning variables
n = int(input()) # number of phrases
phrases = [] # list of phrases
for i in range(n): # for loop to go through each phrase
    phrases.append(input().split()) # append each phrase to the list
Zodiacs = [ # list of zodiacs
	"Ox",
	"Tiger",
	"Rabbit",
	"Dragon",
	"Snake",
	"Horse",
	"Goat",
	"Monkey",
	"Rooster",
	"Dog",
	"Pig",
	"Rat"
]

birthyear = {"Bessie": 0} # dictionary of birth years
# for loop to go through each phrase
for i in range(n): # for loop to go through each phrase
    animal = phrases[i][4] # animal of the first cow
    when = phrases[i][3] # append the when to the list
    name1 = phrases[i][0] # name of the first cow
    name2 = phrases[i][-1] # name of the second cow
    # if the when is "previous"
    if when == "previous":
        year = birthyear[name2] - 1 # subtract 1 from the year
        while(Zodiacs[year % 12] != animal): # while the zodiac is not the animal
            year -= 1 # subtract 1 from the year
    else: # if the when is "next"
        year = birthyear[name2] + 1 # add 1 to the year
        while(Zodiacs[year%12] != animal): # while the zodiac is not the animal
            year += 1 # add 1 to the year
    birthyear[name1] = year # append the year to the list
# output 
print(abs(birthyear["Elsie"]))