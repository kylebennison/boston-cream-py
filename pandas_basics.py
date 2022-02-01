import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

elo = pd.read_csv('https://raw.githubusercontent.com/kylebennison/staturdays/master/Production/elo_ratings_historic.csv')

# Glimpse
elo.info()

# Summary
elo.describe()

# Subset
e21 = elo[elo['season'] == 2021]

e21[(e21['elo_rating'] == e21['elo_rating'].max())]

# Plot

e21.groupby('conference')['elo_rating'].mean().plot(kind = 'barh',
                                                    color = 'Blue')
plt.suptitle('Average Elo in 2021')
plt.xlabel('Elo')
plt.ylabel('Conference')
