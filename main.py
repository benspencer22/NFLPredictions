# NFL Game predictor
# Authors:  Ben Spencer and Tony Hui
# get the libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split


# read in the data
nfl = pd.read_csv('nfl_games.csv')
# print(nfl.describe())

# Team names
TEAMS = ['Cowboys', 'Buccaneers', 'Eagles', 'Falcons', 'Steelers',
         'Bills', 'Jets', 'Panthers', 'Vikings',
         'Bengals', '49ers', 'Lions', 'Jaguars',
         'Seahawks', 'Colts', 'Cardinals', 'Titans',
         'Chargers', 'Commanders', 'Browns', 'Chiefs',
         'Dolphins', 'Patriots', 'Packers', 'Saints',
         'Broncos', 'Bears', 'Rams', 'Raiders', 'Ravens']

# enter the teams you want to predict
home_team = input('Enter the home team: ')
away_team = input('Enter the away team: ')

# get the data for the teams you want to predict
home_data = nfl[(nfl['Team'] == home_team)]
away_data = nfl[(nfl['Team'] == away_team)]

# get the features and the labels
home_features = home_data[['PointsScored', 'PointsGivenUp', 'First Downs', 'NetYards', 'DYards', 'NetRushing',
                           'DRushing', 'NetPassing', 'DPassing', 'Punts', 'Possession', 'NumOfPlays', '3rd Down %',
                           'Outcome']]
away_features = away_data[['PointsScored', 'PointsGivenUp', 'First Downs', 'NetYards', 'DYards', 'NetRushing',
                           'DRushing', 'NetPassing', 'DPassing', 'Punts', 'Possession', 'NumOfPlays', '3rd Down %',
                           'Outcome']]

# drop Outcome column
n_home_data = home_features.drop(['Outcome'], axis=1)
n_away_data = away_features.drop(['Outcome'], axis=1)

# get average scores for the teams you want to predict
home_avg = n_home_data.mean()
away_avg = n_away_data.mean()

# split the data into training and testing
home_train, home_test = train_test_split(n_home_data, test_size=0.2)
away_train, away_test = train_test_split(n_away_data, test_size=0.2)

# create the model


# fit the model


# predict the scores
