""" Simple Chatbot in Python (No Machine Learning) """


import random


# Global vars
USERNAME = None


# helper functions
def print_bot_line(text):
	print(f"BART: {text}")

def input_bot_prompt(text):
	return input(f"BART: {text}")


def greet():
	GREETINS = ["Hello", "Hola", "Bonjour", "Buongiorno", "Hi", "Welcome"]

	welcome_msg = """Greatings! I am BART (Bot Assisting Real Talk) chatbot:)"""
	print_bot_line(welcome_msg)

	USERNAME = input_bot_prompt("What's your name?\n")

	print_bot_line(f"{random.choice(GREETINS)}, {USERNAME}!")


if __name__ == "__main__":
	greet()
