import sys

if len(sys.argv) < 2:
	exit()
if len(sys.argv) > 2:
	print("ERROR")
	exit()
n = sys.argv[1]
try:
	n = int(n)
except ValueError:
	print("ERROR")
	exit()
if n == 0:
	print("I'm Zero")
elif n % 2 == 0:
	print("I'm Even")
else:
	print("I'm Odd")
