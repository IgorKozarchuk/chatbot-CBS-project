""" Simple Chatbot in Python (no Machine Learning) """


import random
import pyjokes
import os.path
import pandas as pd


# Global vars
USERNAME = None


# Helper functions

def print_bot_line(text):
	print(f"BART: {text}")


def input_bot_prompt(text):
	return input(f"BART: {text}")


def print_user_line(text):
	print(f"{USERNAME}: {text}")


def clean_dataset():
	clean_path = "chatbot/TMDB_movie_dataset_clean.csv"

	if not os.path.isfile(clean_path):
		df = pd.read_csv("chatbot/TMDB_movie_dataset.csv")
		# print(df.shape[0])
		# remove movies with 0 score
		df.drop(df[df.vote_score == 0].index, inplace=True)
		# print(df.shape[0])
		df.to_csv(clean_path, index=False)

	# print("clean dataset already exists")


# Main functions

def greet():
	GREETINS = ["Hello", "Hola", "Bonjour", "Buongiorno", "Hi", "Welcome", "Ciao"]

	welcome_msg = """Greatings! I am BART (Bot-Assisted Real Talk) chatbot:)"""
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
									"3 - play a game\n"\
									"0 - EXIT\n"\
									f"{USERNAME}: "
	)

	return user_choice


def tell_joke():
	print_bot_line(pyjokes.get_joke())


def recommend_movie():
	df = pd.read_csv("chatbot/TMDB_movie_dataset_clean.csv")
	# print(df.head())
	print_bot_line("I can recommend you a movie based on genre, year, rating, and tagline.")
	user_genre = input_bot_prompt("- Enter genre: ")
	user_year = input_bot_prompt("- year: ")
	user_rating = input_bot_prompt("- minimal rating: ")
	user_tagline = input_bot_prompt("- tagline keywords: ")

	print(user_year, user_genre, user_rating, user_tagline)


def play_game():
	print_bot_line("Game test")


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
	clean_dataset()

	# greet()
	# main_loop()

	recommend_movie()
