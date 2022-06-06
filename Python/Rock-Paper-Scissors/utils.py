from time import sleep


class Formatting:
  ENDF = '\033[0m'
  BOLD = '\033[1m'
  BOLDITALIC = '\033[1m\033[3m'
  LIGHT = '\033[2m'
  ITALIC = '\033[3m'
  UNDERLINE = '\033[4m'
  INVERT = '\033[7m'
  COLOR_BLACK = '\033[30m'
  COLOR_RED = '\033[31m'
  COLOR_GREEN = '\033[32m'
  COLOR_YELLOW = '\033[33m'
  COLOR_BLUE = '\033[34m'
  COLOR_PURPLE = '\033[35m'
  COLOR_PURPLE = '\033[35m'
  COLOR_CYAN = '\033[36m'
  COLOR_WHITE = '\033[37m'
  BACKGROUND_BLACK = '\033[40m'
  BACKGROUND_RED = '\033[41m'
  BACKGROUND_GREEN = '\033[42m'
  BACKGROUND_YELLOW = '\033[43m'
  BACKGROUND_BLUE = '\033[44m'
  BACKGROUND_PURPLE = '\033[45m'
  BACKGROUND_CYAN = '\033[46m'
  BACKGROUND_WHITE = '\033[47m'


def printMessage(state: str, content: str):
	'''
	Prints a message and styles it based on a specified state
	'''
	if state.lower() == 'error':
			print(f'{Formatting.BOLDITALIC}{Formatting.COLOR_RED}{content}{Formatting.ENDF}')
	elif state.lower() == 'valid':
			print(f'{Formatting.BOLDITALIC}{Formatting.COLOR_GREEN}{content}{Formatting.ENDF}')
	elif state.lower() == 'info':
			print(f'{Formatting.BOLDITALIC}{Formatting.COLOR_CYAN}{content}{Formatting.ENDF}')
	sleep(0.75)


def checkExitIntent(message, positiveAction, negativeAction):
	while True:
		option = input(f'{message}' + '\n>> ').upper()
	
		if option == 'Y' :
			positiveAction()
		elif option == 'N':
			negativeAction()
		else:
			printMessage('invalid', 'Invalid option. Reply Y for [Y]es & N for [N]o')
