from FileLoader import FileLoader
import pandas as pd

class SpatioTemporalData:
	def __init__(self, df):
		self.df = df
	def when(self, location):
		print(list(self.df.loc[ (df['City'] == location)]['Year'].unique()))
	def where(self, date):
		print(list(self.df.loc[ (df['Year'] == date),:]['City'].unique()))

if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("./resources/athlete_events.csv")
	sp = SpatioTemporalData(df)
	sp.where(1896)
	sp.where(2016)
	sp.when('Athina')
	sp.when('Paris')
