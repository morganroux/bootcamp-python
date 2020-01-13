import sys
from random import randint

def check(n):
	global r
	global trial
	if n > r:
		print("Too high")
	elif n < r:
		print("Too low")
	else:
		if trial == 1: print("Congrats ! First Try")
		else: print("Congrats {} try".format(trial))
		exit()

def prompt():
	n = input("What's your guess between 1 and 99?\n>> ")
	if n == 'exit':
		print("Goodbye !")
		exit()
	try:
		n = int(n)
	except ValueError:
		return 0
	check(n)
	return 1
	
r = randint(0, 100)
trial = 1
print("""
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
print(str(r))
while True:
	if prompt() == 0:
		print("That's not a number !")
	trial += 1
