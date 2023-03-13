import sys, math

#opening file and assigning variables
file = open("highcard.in", "r") #open file
n = int(file.readline()) #assigning first line to N (number of cards each cow gets)
#assign n number of cards to a list
cards = set() #empty set of cards
#for loop to assign n number of cards to the list
for i in range(n):
    cards.add(int(file.readline()))
file.close()

#output the max number of rounds Bessie can win
bessiecards = [] #empty list of bessie's cards
elsiecards = [] #empty list of elsie's cards
for i in range(1, (2*n)+1): #for loop to go through each card
    if i not in cards: #if the card is not in elsie's cards
        bessiecards.append(i) #add the card to bessie's cards
    else:
        elsiecards.append(i)
bessiepoints = 0 #bessie's points is 0
bessie_index, elsie_index = 0, 0

#while loop to find the max number of rounds Bessie can win
while bessie_index < n and elsie_index < n:
    if bessiecards[bessie_index] > elsiecards[elsie_index]: #if bessie's card is greater than elsie's card
        bessiepoints += 1 #add 1 to bessie's points
        elsie_index += 1 #add 1 to elsie's index
        bessie_index += 1 #add 1 to bessie's index
    else: #if bessie's card is less than elsie's card
        bessie_index += 1 #add 1 to bessie's index

#output to file
file = open("highcard.out", "w")
file.write(str(bessiepoints))
file.close()