class Evaluator:
	def __init__(self):
		pass
	
	@staticmethod
	def zip_evaluate(coefs, words):
		n = 0
		if len(words) != len(coefs):
			return -1
		for t in zip(coefs, words):
			n += (t[0] * len(t[1]))
		print(n)

	@staticmethod
	def enumerate_evaluate(coefs, words):
		if len(words) != len(coefs):
			return -1

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
