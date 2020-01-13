import sys
import string

dico =	{	'A':'.-', 'B':'-...',
			'C':'-.-.', 'D':'-..', 'E':'.',
			'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
			'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
			'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ' ': ' ' }
def init():
	if len(sys.argv) == 1:
		exit()
	sys.argv.pop(0)
	s = ' '.join(sys.argv).upper()
	for c in s:
		if c not in dico.keys():
			print("ERROR ")
			exit()
	return s

def morse(s):
	lst = []
	for word in s.split():
		lst.append(' '.join( dico[c] for c in word))
	return ' / '.join(lst)

s = init()
m = morse(s)
print(m)
					
