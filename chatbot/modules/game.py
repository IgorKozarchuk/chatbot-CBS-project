import random

from modules import settings
from modules.settings import print_bot_line, input_bot_prompt


def play_game():
	""" Tic-tac-toe game """
	# game board
	board = [[" ", "A", "B", "C"],
			["1", "_", "_", "_"],
			["2", "_", "_", "_"],
			["3", "_", "_", "_"]]
	
	available_cells = []


	def init_available_cells():
		for i in range(1, len(board[0])):
			for j in range(1, len(board[0])):
				if board[i][j] == "_":
					available_cells.append((i,j))


	def update_available_cells(move):
		available_cells.remove(move)


	def print_board(board):
		for row in board:
			for i in row:
				print(i, end=" ")
			print()


	def reset_board(board):
		for i in range(1, len(board[0])):
			for j in range(1, len(board[0])):
				board[i][j] = "_"


	def get_user_move():
		while True:
			user_move = input_bot_prompt(f"To make a move, enter coordinates (e.g. A1, B2)\n{settings.USERNAME}: ").upper()
			if (ord(user_move[0]) not in range(65, 68) or 
				ord(user_move[1]) not in range(49, 52)): # not A, B, C or 1, 2, 3
				print_bot_line("Wrong coordinates.")
				continue
			return user_move


	def make_user_move(user_move):
		move_coords = (ord(user_move[0])-64, ord(user_move[1])-48) # from ASCII code to board coords

		if (board[move_coords[1]][move_coords[0]] == "X" or
			board[move_coords[1]][move_coords[0]] == "0"): # if square is occupied
			print_bot_line("The square is occupied. Try again.")
			make_user_move(get_user_move())

		board[move_coords[1]][move_coords[0]] = "X"

		update_available_cells(move_coords)
		print_board(board)


	def make_bot_move():
		print_bot_line("My turn")

		bot_move = random.choice(available_cells)
		board[bot_move[1]][bot_move[0]] = "0"
		update_available_cells(bot_move)
		
		print_board(board)


	def game_loop():
		print_bot_line("Let's play a Tic-Tac-Toe game!")
		print_board(board)
		init_available_cells()

		for i in range(3):
			make_user_move(get_user_move())
			make_bot_move()


	game_loop()
