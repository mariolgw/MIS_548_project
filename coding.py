import pandas as pd
import numpy as np

## here are some basic lines of code for prelim analysis

players = pd.read_csv('NFL Players data.csv')

players.head()

players.dtypes
print(players[['Height','Weight']].describe())