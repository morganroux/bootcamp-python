class Vector:
	def __init__(self, param):
		if isinstance(param, int):
			self.size = param
			self.values = [float(x) for x in range(0, param)]
		elif isinstance(param, list) and all(isinstance(x, float) for x in param):
			self.values = param
			self.size = len(param)
		elif isinstance(param, tuple) and all(isinstance(x, int) for x in param) and len(param) == 2:
			self.values = [float(x) for x in range(param[0], param[1])]
			self.size = len(self.values)
		else:
			print("ERROR init Vector")
	
	def __add__(self, other):
		return Vector([self.values[i] + other.values[i] for i in range(self.size)])
