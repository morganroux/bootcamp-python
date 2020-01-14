def generator(text, sep=" ", option=None):
	lst = text.split(sep)
	if option == None:
		for word in lst:
			yield word
	elif option == 'shuffle':
		for word in lst[::-1]:
			yield word
	elif option == 'sorted':
		for word in sorted(lst, key=lambda w: str.lower(w)):
			yield word
