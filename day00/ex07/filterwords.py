import sys
import string 

def init():
	if len(sys.argv) != 3:
		print("ERROR")
		exit()
	s = sys.argv[1]
	n = sys.argv[2]
	if s.isdigit():
		print("ERROR")
		exit()
	try:
		n = int(n)
	except ValueError:
		print("ERROR")
		exit()
	return s, n

def print_filter(s, n):
	lst = []
	s = ''.join(c for c in s if c not in string.punctuation)
	for word in s.split():
		if len(word) >= n and not word in string.punctuation:
			lst.append(word)
	print(lst)
		
s, n = init()
print_filter(s, n)
