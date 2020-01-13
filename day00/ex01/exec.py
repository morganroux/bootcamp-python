import sys

if len(sys.argv) == 1:
	exit()
sys.argv.pop(0)
str = sys.argv[0]
sys.argv.pop(0)
for arg in sys.argv:
	str = str + ' ' + arg

str = str[::-1]
str = str.swapcase()
print(str)
