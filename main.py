import pandas
from pandas import DataFrame

teams = [" ","El pickles", "why are we playing this professionally", "the pickles", "p i c k l e", "theamazingfluffyrainbowunicornsthatplaypickleball"]

wins = [" ","4", "6", "19", "123", "-2"]

dataset = list(zip(teams, wins))

df = DataFrame(data = dataset, columns = ["teams", "wins"])

#print(dataset)
print(df)