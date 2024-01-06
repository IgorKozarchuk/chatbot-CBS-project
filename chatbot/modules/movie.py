import os.path
import pandas as pd

from modules.settings import print_bot_line, input_bot_prompt


def clean_dataset():
	clean_path = "chatbot/data/TMDB_movie_dataset_clean.csv"

	if not os.path.isfile(clean_path):
		df = pd.read_csv("chatbot/data/TMDB_movie_dataset.csv")
		# remove movies with 0 score
		df.drop(df[df.vote_score == 0].index, inplace=True)
		# remove fows with empty values
		df.dropna(inplace=True)
		# save to a new file
		df.to_csv(clean_path, index=False)


def recommend_movie():
	df = pd.read_csv("chatbot/data/TMDB_movie_dataset_clean.csv") # dataframe

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
