import sys
import os
from Lexer import *


def getcontents(filename: str) -> str:
	with open(filename, "r") as src:
		return src.read()

def tokenize(contents: str):
	lexer = Lexer(contents)
	tokens = lexer.make_tokens()

	if isinstance(tokens, Error):
		print(tokens.as_string())
		exit(1)
	else:
		return tokens


if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} <file> ..")
	exit(1)

for i in sys.argv:
	if not os.path.exists(i):
		print(f"The path \"{i}\" does not exist.")
		exit(1)

	if sys.argv[0] != i:
		contents = getcontents(i)
		print(tokenize(contents))
