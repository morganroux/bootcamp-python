import pandas as pd

class FileLoader:
	def __init__(self):
		pass
	def load(self, path): return pd.read_csv(path)
	def display(self, df, n): 
		pd.set_option('display.max_rows', None)
		print(df.head(n) if n > 0 else df.tail(-n))

if __name__ == "__main__":
		fl = FileLoader()
		df = fl.load("./resources/athlete_events.csv")
		fl.display(df, -10)
