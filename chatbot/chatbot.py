""" Simple Chatbot in Python (no ML or AI) """


import random

from modules import settings
from modules.settings import print_bot_line, input_bot_prompt, print_user_line
from modules.joke import tell_joke
from modules.movie import clean_dataset, recommend_movie
from modules.game import play_game


# Main functions

def greet():
	GREETINS = ["Hello", "Hola", "Bonjour", "Buongiorno", "Hi", "Welcome", "Ciao"]

	welcome_msg = """Greetings! I am BART (Bot-Assisted Real Talk) chatbot:)"""
	print_bot_line(welcome_msg)

	settings.USERNAME = input_bot_prompt("What's your name? ")

	print_bot_line(f"{random.choice(GREETINS)}, {settings.USERNAME}!")


def select_activity():
	print()

	user_choice = input_bot_prompt("What do you want to do? Select an activity:\n"\
									"1 - tell a joke\n"\
									"2 - recommend a movie\n"\
									"3 - play a game\n"\
									"0 - EXIT\n"\
									f"{settings.USERNAME}: "
	)

	return user_choice


def say_bye():
	BYES = ["Bye!", "Good bye!", "See you...", "Ciao", "Arrivederci", "Hasta la vista"]

	print_bot_line(random.choice(BYES))


# main loop
def main_loop():
	while True:
		match select_activity():
			case "1":
				tell_joke()
			case "2":
				recommend_movie()
			case "3":
				play_game()
			case "0":
				say_bye()
				break
			case _:
				continue


if __name__ == "__main__":
	settings.init()
	clean_dataset()
	greet()
	main_loop()
