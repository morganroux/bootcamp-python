from FileLoader import FileLoader
import pandas as pd

def howManyMedals(df, name):
	dict = {}
	nm = df.loc[df['Name'] == name, ['Year', 'Medal']]
	for year in pd.unique(df['Year'].sort_values()):
		yr = nm.loc[df['Year'] == year, ['Medal']]
		g = yr.loc[ df['Medal'] == 'Gold', :].count()['Medal']
		s = yr.loc[ df['Medal'] == 'Silver', :].count()['Medal']
		b = yr.loc[ df['Medal'] == 'Bronze', :].count()['Medal']
		if (g,s,b) != (0,0,0):
			dict[year] = { 'g' : g, 's' : s, 'b' : b }
		
	print(dict)

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("./resources/athlete_events.csv")
	howManyMedals(data, 'Kjetil Andr Aamodt')
