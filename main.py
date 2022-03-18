from random import randint

board = []
turn = "X"
players = {"X":"", "O":""}

def setBoardValue(x,y):
	board[x][y] = turn

def switchTurn():
	global turn 
	if turn == "X":
		turn = "O" 
	else: 
		turn = "X"
		
def printHorizontalRule():
	print("―――――――――――")

def printLine(n):
	print(" "+board[n][0]+" | "+board[n][1]+" | "+board[n][2])

def printBoard():
	printLine(0)
	printHorizontalRule()
	printLine(1)
	printHorizontalRule()
	printLine(2)
	print()

def setupPlayersName():
	global players
	player1_name = input("Player 1 name: ")
	print("Welcome "+(player1_name))
	player2_name = input("Player 2 name: ")
	print("Welcome "+(player2_name))
	print ("Flipping coin...")
	whoGoesFirst = randint(0,1)
	
def setupBoard():
	global board
	board = [
		[" "," "," "],
		[" "," "," "],
		[" "," "," "]
	]

def isPlayersNamesSet():
	return players["X"] != "" and players["O"] != ""

def setupGame():
	setupBoard()
	if (not isPlayersNamesSet()):
		setupPlayersName()

def printMainMenu():
	print ("[1] Start PvP match")
	print ("[q] Quit")

def mainMenu():
	printMainMenu()
	return input()

def playGame():
	global turn 
	global players 
	print()
	print (players)
	print("The game!")
	printBoard()
	print (players [turn] + ", where do you want to put your " + turn + "?")

def main():
	while True:
		userInput = mainMenu()
		if userInput == "1":
			setupGame()
			playGame()
		elif userInput == "q":
			break
		else:
			print("Command not found.")


main()