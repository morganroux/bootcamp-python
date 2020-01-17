from FileLoader import FileLoader
import pandas as pd

def howManyMedalsByCountry(df, country):
	dict = {}
	for year in pd.unique(df['Year'].sort_values()):
		medals = df.loc[ (df['NOC'] == country) & (df['Year'] == year), ['Event', 'Medal']].drop_duplicates()
		g = medals.loc[df['Medal'] == "Gold", :].count()['Medal']
		s = medals.loc[df['Medal'] == "Silver", :].count()['Medal']
		b = medals.loc[df['Medal'] == "Bronze", :].count()['Medal']
		dict[year] = {"G" : g, "S" : s, "B" : b}
	print(dict)
if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("./resources/athlete_events.csv")
	howManyMedalsByCountry(df, 'FRA')
