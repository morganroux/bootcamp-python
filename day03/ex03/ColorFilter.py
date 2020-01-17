import numpy as np

class ColorFilter:
	def __init__(self):
		pass
	def invert(self, array):
		if array.shape[2] == 3:
			return 1 -  array
		else:
			return (1,1,1,0) + array * (-1, -1, -1, 1)
	def to_blue(self, array):
		arr = np.zeros(array.shape)
		arr[::,::,2] = array[::,::,2]
		if array.shape[2] == 4:
			arr[::,::,3] = array[::,::,3]
		return arr
	def to_green(self, array):
		if array.shape[2] == 3:
			return array * (0,1,0)
		else:
			return array * (0,1,0,1)
	def to_red(self, array):
		if array.shape[2] == 3:
			return array - self.to_green(array) - self.to_blue(array)
		else:
			return array - self.to_green(array) * (1,1,1,0) - self.to_blue(array) * (1,1,1,0)
	def celluloid(self, array, t):
		arr = np.ones(array.shape)
		arr[:,:,3] = array[:,:,3]
		thrs = np.linspace(0, 1, t)
		for n in range(3):
			for i, th in enumerate(thrs[1:]):
				idx = np.logical_and((array[:,:,n] >= thrs[i]), (array[:,:,n] < th)) 
				arr[idx, n] = thrs[i]
		return arr
	
	def to_greyscale(self, array, option = 'm'):
		arr = np.copy(array)
		if option == 'm' :
			arr[:,:,0:3] = np.stack( ((np.sum(arr, where=[True, True, True, False], axis = 2) / 3), ) * 3, -1)
		if option == 'weighted':
			arr[:,:,0:3] = np.stack( ((np.sum(arr * (0.299,0.587,0.114, 0) , where=[True, True, True, False], axis = 2) / 3), ) * 3, -1)
		return arr
