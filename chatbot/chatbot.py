""" Simple Chatbot in Python (No Machine Learning) """


import random
import pyjokes


# Global vars
USERNAME = None


# Helper functions

def print_bot_line(text):
	print(f"BART: {text}")

def input_bot_prompt(text):
	return input(f"BART: {text}")

def print_user_line(text):
	print(f"{USERNAME}: {text}")


# Main functions

def greet():
	GREETINS = ["Hello", "Hola", "Bonjour", "Buongiorno", "Hi", "Welcome", "Ciao"]

	welcome_msg = """Greatings! I am BART (Bot Assisting Real Talk) chatbot:)"""
	print_bot_line(welcome_msg)

	global USERNAME
	USERNAME = input_bot_prompt("What's your name?\n"\
								f"Username: ")

	print_bot_line(f"{random.choice(GREETINS)}, {USERNAME}!")


def select_activity():
	print_bot_line("What do you want to do?")

	user_choice = input_bot_prompt("Select an activity:\n"\
									"1 - tell a joke\n"\
									"2 - recommend a movie\n"\
									"3 - ...\n"\
									"0 - EXIT\n"\
									f"{USERNAME}: "
	)

	return user_choice


def tell_joke():
	print_bot_line(pyjokes.get_joke())


def say_bye():
	BYES = ["Bye!", "Good bye!", "See you...", "Ciao", "Arrivederci", "Hasta la vista"]

	global USERNAME

	print_bot_line(random.choice(BYES))


# main loop
def main_loop():
	user_choice = None

	while True:
		user_choice = select_activity()
		match user_choice:
			case "1":
				tell_joke()
			case "0":
				say_bye()
				break
			case _:
				continue


if __name__ == "__main__":
	greet()
	main_loop()
