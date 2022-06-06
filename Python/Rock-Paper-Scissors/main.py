import re
from time import sleep
from random import choice as selectRandomOption
from utils import Formatting as Style, printMessage, checkExitIntent


USER_SCORE = 0
COMPUTER_SCORE = 0

def init():
	welcomeMessage = '[ Welcome To The Rock/Paper/Scissors CLI™ ! ]'
	print('\n' + Style.BACKGROUND_BLUE + Style.COLOR_WHITE + Style.BOLD + welcomeMessage + Style.ENDF)
	print('—' * len(welcomeMessage), '\n', end='')
	showActions()


def getAction():
	# Shows the list of possible options to a user and returns the chosen option
	print()
	i = 1; actions = ['Start Game', 'Game Rules', 'About', 'Exit']

	for action in actions:
		print(f'{Style.BOLDITALIC}{i}. {Style.COLOR_CYAN}{action}{Style.ENDF}')
		sleep(0.1)
		i += 1

	while True:
		action = None
		try:
			action = int(styledInput('Select an option'))
		except ValueError:
			printMessage('error', 'Error: Enter a valid option!')
			continue
		if action < 1 or action > len(actions):
			printMessage('error', 'Error: Enter a valid option!')
			continue
		else:
			break

	return action


def showActions():
	action = getAction()
	if action == 1:
		playGame()
	elif action == 2:
		printGameRules()
	elif action == 3:
		about()
	elif action == 4:
		exit()


def styledInput(content: str):
	# Styles the user input prompt and exits the app if the input == "quit" or goes to the main menu if input == "menu"
	exitHint = f'\n{Style.ITALIC}{Style.COLOR_YELLOW}** Hint: Type "menu" to access the main menu or "quit" to exit the app instantly{Style.ENDF}'
	userInput = input(f'{exitHint}{Style.COLOR_PURPLE}{Style.ITALIC}\n{content}:{Style.ENDF}\n>> ')
	if userInput.lower() == 'quit':
		quit()
	elif userInput.lower() == 'menu':
		showActions()
	else:
		return userInput


def about():
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n✱  About ✱{Style.ENDF}')
	print(f'{Style.BOLDITALIC}{Style.COLOR_PURPLE}\n>> Task: Rock/Paper/Scissors CLI \n>> Author: (@chizzi01) \n>> Date: 31st May, 2022{Style.ENDF}')
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n© 2022, I4G x Zuri \n{Style.ENDF}')
	# ➝ ➝ ➝
	sleep(5)
	showActions()


def exit():
	'''
	Confirms a user's choice to exit the app
	'''
	global USER_SCORE
	global COMPUTER_SCORE

	while True:
		option = input(f'\n{Style.BOLDITALIC}{Style.COLOR_RED}Are you sure you want to exit?{Style.ENDF} ([Y]es / [N]o)\n>> ').upper()

		if option == 'Y':
			print(f'\n{Style.COLOR_PURPLE}{Style.BOLD}Your Score ⛨ : [{USER_SCORE}]  /  {Style.ENDF}', end='')
			print(f"{Style.COLOR_RED}{Style.BOLD}System's Score ⛨ : [{COMPUTER_SCORE}]{Style.ENDF}")
			printMessage('info', 'Hope you had a nice experience! Have a nice day :)')
			quit()
		elif option == 'N':
			showActions()
		else:
			printMessage('error', '\nInvalid option. Reply Y for [Y]es & N for [N]o')


def printGameRules():
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n✱  The players may count aloud to three, or speak the name of the game (e.g. "Rock! Paper! Scissors! ✱{Style.ENDF}')
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n✱  either raising one hand in a fist and swinging it down with each syllable or holding it behind their back. ✱{Style.ENDF}')
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n✱  They then "throw" by extending it towards their opponent. ✱{Style.ENDF}')
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n✱  Variations include a version where players throw immediately on the third count (thus throwing on the count of "Scissors! ✱{Style.ENDF}')
	print(f'{Style.BOLD}{Style.COLOR_BLUE}\n✱  or a version where they shake their hands three times before throwing. ✱{Style.ENDF}')
		# ➝ ➝ ➝
	# sleep(5)
	showActions()

	# TODO: :)


def printGamePlay(options, selectedOption, computersOption):
	global USER_SCORE
	global COMPUTER_SCORE

	print(f'\n{Style.COLOR_PURPLE}{Style.BOLD}You Chose: [{options[selectedOption]}]  /  {Style.ENDF}', end='')
	print(f"{Style.COLOR_RED}{Style.BOLD}System Chose: [{options[computersOption]}]{Style.ENDF}")
	print(f'{Style.COLOR_PURPLE}{Style.BOLD}Your Score ⛨ : [{USER_SCORE}]  /  {Style.ENDF}', end='')
	print(f"{Style.COLOR_RED}{Style.BOLD}System's Score ⛨ : [{COMPUTER_SCORE}]{Style.ENDF}")


def playGame():
	global USER_SCORE
	global COMPUTER_SCORE

	options = { 'R': 'Rock', 'P': 'Paper', 'S': 'Scissors' }
	selectedOption = None
	computersOption = selectRandomOption(list(options))
	# print("Computer's Option", computersOption) # Cheat Mode
	
	while True:
		selectedOption = styledInput('Enter an option: R for [R]ock, P for [P]aper or S for [S]cissors').upper()
		if not len(selectedOption) or re.match(r'\s', selectedOption):
			printMessage('error', "Error: Input can't be empty!")
			continue
		if not selectedOption in options:
			printMessage('error', "Error: Enter a valid option!")
			continue
		break
	
	if selectedOption == computersOption:
		drawMessages = ["You drew with the system.", "That's a draw!!!", "Oops. A draw. Must be an artist :)"]
		printMessage('info', f'\n❖  {selectRandomOption(drawMessages)}')
		printGamePlay(options, selectedOption, computersOption)

		playGame()
		# checkExitIntent(f'{Style.ITALIC}{Style.COLOR_YELLOW}Do you want to play again? Reply Y for [Y]es & N for [N]o{Style.ENDF}', playGame, exit)
	
	while True:
		# Rock beats Scissors
		# Paper beats Rock
		# Scissors beats Paper
		if selectedOption == 'R' and computersOption == 'S' or selectedOption == 'P' and computersOption == 'R' or selectedOption == 'S' and computersOption == 'P':
			USER_SCORE += 1
			winMessages = ["You freaking won!", "Yay yeh! That's a good chap!", "Yup. You deserve a medal :)"]
			printMessage('info', f'\n✦  {selectRandomOption(winMessages)}')
			printGamePlay(options, selectedOption, computersOption)

			playGame()
			# checkExitIntent(f'{Style.ITALIC}{Style.COLOR_YELLOW}Do you want to play again? Reply Y for [Y]es & N for [N]o{Style.ENDF}', playGame, exit)
		
		if computersOption == 'R' and selectedOption == 'S' or computersOption == 'P' and selectedOption == 'R' or computersOption == 'S' and selectedOption == 'P':
			COMPUTER_SCORE += 1
			failMessages = ["You freaking lost!", "Whew! Try again please.", "Tch. Better luck next time :)"]
			printMessage('error', f'\n✖  {selectRandomOption(failMessages)}')
			printGamePlay(options, selectedOption, computersOption)

			playGame()
			# checkExitIntent(f'{Style.ITALIC}{Style.COLOR_YELLOW}Do you want to play again? Reply Y for [Y]es & N for [N]o{Style.ENDF}', playGame, exit)

init()