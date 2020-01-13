import sys

def init():
	if len(sys.argv) > 3:
		print("InputError: too many arguments")
	if len(sys.argv) != 1:
		print("""
Usage: python operations.py
Example:
	python operations.py 10 3""")
		exit()
	
	return int(sys.argv[1]), int(sys.argv[2])

def sum(x, y):
	return str(x + y)
def diff(x, y):
	return str(x - y)
def prod(x, y):
	return str(x * y)
def div(x, y):
	if y == 0:
		return "ERROR (div by zero)"
	return str(x / y)
def mod(x, y):
	if y == 0:
		return "ERROR (modulo by zero)"
	return str(x % y)
def print_result(x, y):
	print("sum : " + sum(x, y) + "\ndiff : " + diff(x, y) + "\nprod : " + prod(x, y) + "\ndiv : " + div(x, y) + "\nmod : " + mod(x, y)) 

a, b = init()
print_result(a, b)

