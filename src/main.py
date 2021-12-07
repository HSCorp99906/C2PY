import sys
import os


def getcontents(filename: str) -> str:
	with open(filename, "r") as src:
		return src.read()


for i in sys.argv:
	if not os.path.exists(i):
		print(f"The path \"{i}\" does not exist.")
		exit(1)

	if i != "main.py":


