import numpy as np

class ScrapBooker:
	def __init__(self):
		pass
	def crop(self, array, dimensions, position = (0,0)):
		for i,j,k in zip(array.shape, dimensions, position):
				if i < j + k:
						print("error")
						return array
		sl = [slice(position[i], position[i] + dimensions[i]) for i in range(len(position))]
		return array[tuple(sl)]
	def thin(self, array, n, axis): return np.delete(array, n, axis)
	def juxtapose(self, array, n, axis): return np.concatenate(tuple([array]) * n, axis)
	def mosaic(self, array, dimensions):
		arr = array
		for i, n in enumerate(dimensions):
				print(i, n)
				arr = np.concatenate(tuple([arr]) * n, i)
		return arr
		
	
if __name__ == "__main__":
	sc = ScrapBooker()
	arr = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
	arr2 = sc.crop(arr, (2,3), (1,0))
	print(arr)
	print(arr2)
