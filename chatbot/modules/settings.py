# Global settings

def init():
	global USERNAME
	USERNAME = None


# Helper functions

def print_bot_line(text):
	print(f"BART: {text}")

def input_bot_prompt(text):
	return input(f"BART: {text}")

def print_user_line(text):
	print(f"{USERNAME}: {text}")
