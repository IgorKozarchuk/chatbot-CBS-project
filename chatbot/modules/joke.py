import pyjokes

from modules.settings import print_bot_line


def tell_joke():
	print_bot_line(pyjokes.get_joke())
