""" Simple Chatbot in Python (no ML or AI) """


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
		# remove movies with 0 score
		df.drop(df[df.vote_score == 0].index, inplace=True)
		# remove fows with empty values
		df.dropna(inplace=True)
		# save to a new file
		df.to_csv(clean_path, index=False)


# Main functions

def greet():
	GREETINS = ["Hello", "Hola", "Bonjour", "Buongiorno", "Hi", "Welcome", "Ciao"]

	welcome_msg = """Greetings! I am BART (Bot-Assisted Real Talk) chatbot:)"""
	print_bot_line(welcome_msg)

	global USERNAME
	USERNAME = input_bot_prompt("What's your name?\n"\
								f"Username: ")

	print_bot_line(f"{random.choice(GREETINS)}, {USERNAME}!")


def select_activity():
	print()

	user_choice = input_bot_prompt("What do you want to do? Select an activity:\n"\
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
	df = pd.read_csv("chatbot/TMDB_movie_dataset_clean.csv") # dataframe

	print_bot_line("I can recommend you a movie based on a genre, year and rating.")
	user_genre = input_bot_prompt("- Enter genre: ").title() # e.g. Drama
	user_years = [int(x) for x in input_bot_prompt("- year range (space separated): ").split(maxsplit=1)] # e.g. [1995, 2000]
	user_rating = int(input_bot_prompt("- minimal rating: ")) # e.g. 8
	
	# filter movies
	recommended_movies_df = pd.DataFrame(columns=df.columns)
	LIST_MAX_LENGTH = 10

	for i in range(len(df.index)):
		if (user_rating <= df.iloc[i]["vote_score"] and
			(user_years[0] <= int(df.iloc[i]["release_date"][-4:]) and user_years[1] >= int(df.iloc[i]["release_date"][-4:])) and
			user_genre in df.iloc[i]["genres"]):
			# https://stackoverflow.com/questions/44156051/add-a-series-to-existing-dataframe
			recommended_movies_df = pd.concat([recommended_movies_df, df.iloc[i].to_frame().T], ignore_index=True)
	
	if recommended_movies_df.empty:
		print_bot_line("Sorry, no matching movies found:(")
		return

	print_bot_line("Here is the list of top rated recommended movies:")
	print(recommended_movies_df.iloc[:, 1:].sort_values(by="vote_score", ascending=False).head(LIST_MAX_LENGTH).to_string(index=False))


def play_game():
	print_bot_line("Game test")


def say_bye():
	BYES = ["Bye!", "Good bye!", "See you...", "Ciao", "Arrivederci", "Hasta la vista"]

	global USERNAME

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
	clean_dataset()
	greet()
	main_loop()
