import pandas as pd
import numpy as np
import sys
#print(sys.version)

players = pd.read_csv('NFL Players data.csv')

print(players.head())

print(players.dtypes)

missing_val = players.isnull().sum()
stats = players.describe()

print(missing_val)
print(stats, '\n')
print(players.shape)

df = players.drop(['middleName', 'suffix', 'status', 'jerseyNumber'], axis = 1)
print(df.isnull().sum())
print(df.tail())

ids = df['nflId']
print(ids)

unique = df['nflId'].value_counts()
results = unique.to_dict()
results[182]

# write a program to preseve only 1 record of each player
def unique_players(df):
    unique = df['nflId'].value_counts()
    results = unique.to_dict()
    results[182]
    return results

unique_players(df)
