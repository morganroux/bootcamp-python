from FileLoader import FileLoader
import pandas as ps

def youngestFellah(df, year):
	fem = df.loc[	
		(df['Sex'] == 'F') & (df['Year'] == year) & (df['Medal'] == 'Gold') , 
		:
	]
	mal = df.loc[	
		(df['Sex'] == 'M') & (df['Year'] == year) & (df['Medal'] == 'Gold') , 
		:
	]

	#print(fem.loc[ fem['Age'] == fem['Age'].min(), :])
	#print(mal.loc[ mal['Age'] == mal['Age'].min(), :])
	return { 'f' : fem['Age'].min(), 'm' : mal['Age'].min()}

if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("./resources/athlete_events.csv")
	print(youngestFellah(df, 2004))
