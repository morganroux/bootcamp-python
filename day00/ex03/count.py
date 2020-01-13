import sys
import string 

def text_analyzer(s = ''):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	upper = lower = punct = space = total = 0
	if s == '':
		s = input("texte ?")
	for c in s:
		total += 1
		if c.isupper():
			upper += 1
		elif c.islower():
			lower += 1
		elif c in string.punctuation:
			punct += 1
		elif c == ' ':
			space += 1
	print("total : " + str(total) + "\nupper : " + str(upper) + "\nlower : " + str(lower) + "\npunct : " + str(punct) + "\nspace : " + str(space))
