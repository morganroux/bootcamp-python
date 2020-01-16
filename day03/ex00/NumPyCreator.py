import numpy as np

class NumPyCreator:
	def __init__(self):
		pass
	def from_list(self, lst): return np.array(lst)
	def from_tuple(self, tpl): return np.array(list(tpl))
	def from_iterable(self, itr): return np.array(itr)
	def from_shape(self, shape, value): return np.ones(shape) * value
	def random(self, shape): return np.empty(shape)
	def identity(self, n): return np.identity(n)


