def choosepath(numberofpaths):
	choice = 0
	while choice < 1 or choice > numberofpaths:
		print ("1 to " + str(numberofpaths) + "> ", end="")
		choice = input()
		if choice != "1" and choice != "2":
			choice = 0
		if choice == "1" or choice == "2":
			choice = int(choice)
	print()
	return choice

def pause():
	print("press enter to continue.")
	input()

def intro():
	print ("Welcome to the Tomb of Nazerick young adventurer!")
	print ("You are young but addventurous and full of spirit, but be warned this tomb you entered may be your last.")
	print ("Many traps and trials await you if you wish to survive and the sacred treasure room, FORTUNE AND GLORY TO YOU!")
	pause()
	beginning()
	
def beginning():
	print ("The Tomb of Nazerick stands before you and you begin to descend down its cold stairwell.")
	print ("Skeletons and ashy remains of travelers and graverobbers past decorate the mausoleum.")
	print ("As you reach the first level you hear clattering of bones and see shadows forming from around the corner, along with bone piles littering room")
	print ("What do you do?")
	print (" 1 = engage the skeletal abominations!")
	print (" 2 = your more of a thief than a fighter, hide in the bone piles")
	path = choosepath(2)
	if path == 1:
		engage()
	if path == 2:
		hide()

def engage():
	print ("you charge at the skeletons only to be overpowered by their bony forms and are soon another decoration to the tomb")
	death()
	
def hide():
	print ("You watch as the skeletal abominations pass by making boner jokes and other nonsense, and then continue to the lower floor as theyre not looking.")
	end()

def end ():
	print ("The dungeon was surprisingly tiny and you already reached the treasure room, what a joke!")
	death()

def death():
	print("c'est la vie")
	pause()
	

while True:
	intro()
	print('Would you like to play again? Y/N')
	playAgain = input()
	if playAgain == 'Y' or playAgain == 'y':
		continue
	if playAgain == 'N' or playAgain == 'n':
		break
	break