import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:
	def __init__(self):
		pass
	def load(self, path): return mpimg.imread(path)

	def display(self, array):
		plt.imshow(array)
		plt.show()
