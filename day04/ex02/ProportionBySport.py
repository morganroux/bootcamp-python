from FileLoader import FileLoader
import pandas as ps

def	proportionBySport(df, year, sport, sex):
	p =	(df.loc[ (df['Year'] == 2004) & (df['Sex'] == 'F') & (df['Sport'] == 'Tennis'), :].nunique()['Name'] /
 		df.loc[ (df['Year'] == 2004) & (df['Sex'] == 'F'), :].nunique()['Name']
		* 100)
	print (p)

if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("./resources/athlete_events.csv")
	proportionBySport(df, 2004, 'Tennis', 'F')
