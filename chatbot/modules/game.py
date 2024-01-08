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


	def print_board():
		for row in board:
			for i in row:
				print(i, end=" ")
			print()


	def reset_board():
		for i in range(1, len(board[0])):
			for j in range(1, len(board[0])):
				board[i][j] = "_"


	def init_available_cells():
		available_cells.clear()
		for i in range(1, len(board[0])):
			for j in range(1, len(board[0])):
				available_cells.append((i,j))


	def update_available_cells(move):
		available_cells.remove(move)


	def check_win_condition():
			# rows
		if (board[1][1] == board[1][2] == board[1][3] == "X" or
			board[2][1] == board[2][2] == board[2][3] == "X" or
			board[3][1] == board[3][2] == board[3][3] == "X" or
			# columns
			board[1][1] == board[2][1] == board[3][1] == "X" or
			board[1][2] == board[2][2] == board[3][2] == "X" or
			board[1][3] == board[2][3] == board[3][3] == "X" or
			# diagonals
			board[1][1] == board[2][2] == board[3][3] == "X" or
			board[1][3] == board[2][2] == board[3][1] == "X"):
			return 1 # X win
		
		if (board[1][1] == board[1][2] == board[1][3] == "0" or
			board[2][1] == board[2][2] == board[2][3] == "0" or
			board[3][1] == board[3][2] == board[3][3] == "0" or

			board[1][1] == board[2][1] == board[3][1] == "0" or
			board[1][2] == board[2][2] == board[3][2] == "0" or
			board[1][3] == board[2][3] == board[3][3] == "0" or

			board[1][1] == board[2][2] == board[3][3] == "0" or
			board[1][3] == board[2][2] == board[3][1] == "0"):
			return 2 # 0 win


	def make_user_move():
		user_move = input_bot_prompt(f"To make a move, enter coordinates (e.g. A1, B2)\n{settings.USERNAME}: ")
		user_move = user_move.strip()

		if len(user_move) != 2:
			return make_user_move()

		user_move = user_move.upper()

		if (ord(user_move[0]) not in range(65, 68) or 
			ord(user_move[1]) not in range(49, 52)): # not A, B, C or 1, 2, 3
			print_bot_line("Wrong coordinates.")
			return make_user_move()
			
		move_coords = (ord(user_move[1])-48, ord(user_move[0])-64) # from ASCII code to board coords

		if (board[move_coords[0]][move_coords[1]] == "X" or
			board[move_coords[0]][move_coords[1]] == "0"): # if square is occupied
			print_bot_line("The square is occupied. Try again.")
			return make_user_move()
			
		board[move_coords[0]][move_coords[1]] = "X"

		update_available_cells(move_coords)
		print_board()

		if not available_cells:
			if not check_win_condition():
				return 3 # draw
		
		return check_win_condition()

	
	def make_bot_move():
		print_bot_line("My turn")

		bot_move = random.choice(available_cells)
		board[bot_move[0]][bot_move[1]] = "0"

		update_available_cells(bot_move)
		print_board()
		
		if not available_cells:
			if not check_win_condition():
				return 3 # draw
		
		return check_win_condition()


	def check_game_over(move_result):
		match move_result:
			case 1: # X win (user win)
				print_bot_line("Congrats, you win!")
				return True
			case 2: # 0 win (bot win)
				print_bot_line("I win!")
				return True
			case 3: # draw
				print_bot_line("It's a draw.")
				return True


	def game_loop():
		while True:
			if check_game_over(make_user_move()):
				break
			if check_game_over(make_bot_move()):
				break


	def run_game():
		print_bot_line("Let's play a Tic-Tac-Toe game!")
			
		print_board()
		init_available_cells()
		game_loop()
		reset_board()

		answer = input_bot_prompt("Play again? (y/n): ").lower()
		if answer == "y":
			run_game()
	
	run_game()
