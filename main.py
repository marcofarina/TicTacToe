player1_name = ""
player2_name = ""
board = []

def setupPlayersName():
	global player1_name
	player1_name = input("Player 1 name: ")
	print("Welcome "+(player1_name))
	global player2_name
	player2_name = input("Player 2 name: ")
	print("Welcome "+(player2_name))

def setupBoard():
	global board
	board = [
		["","",""],
		["","",""],
		["","",""]
	]

 una nuova feature del codice

def isPlayersNamesSet():
	return player1_name != "" and player2_name != ""

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
	print("The game!")

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
	
	