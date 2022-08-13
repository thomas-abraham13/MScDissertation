# Used to predicts specified range of past NBA Games
# Execute: python makePastPredictions.py

import pickle
import pandas as pd

from createModel import getTrainingSet, createDataFrame, performLogReg
from configureCWD import setCurrentWorkingDirectory


# Exports game information for all games between specified time period to 'data' Folder within project
def getTrainingSetCSV(startYear, startMonth, startDay, endYear, endMonth, endDay, season, startDateOfSeason, filename='gamesWithInfo.csv'):

    # Gets date, teams, and z-score difs for every game within range
    rangeOfGames = getTrainingSet(startYear, startMonth, startDay, endYear, endMonth, endDay, season, startDateOfSeason)
    rangeOfGamesDataframe = createDataFrame(rangeOfGames)
    accucheck = performLogReg(rangeOfGamesDataframe)

    setCurrentWorkingDirectory('data')

    rangeOfGamesDataframe.to_csv(filename)

# Creates a csv file that gives predictions for range of games
# Prints accuracy of model in predicting games for specified range
def getPredictionsCSV(gameDataFilename, outputFilename):

    setCurrentWorkingDirectory('Data')

    gamesWithZScoreDifs = pd.read_csv(gameDataFilename)

    withoutNums = gamesWithZScoreDifs.loc[:, 'Home':'Date']
    justZScoreDifs = gamesWithZScoreDifs.loc[:, 'W_PCT':'TS_PCT']

    setCurrentWorkingDirectory('models')
    with open('model.pkl', 'rb') as file:  # Change filename here if model is altered
        pickleModel = pickle.load(file)

    predictions = pickleModel.predict(justZScoreDifs)  # Creates list of predicted winners and losers
    probPredictions = pickleModel.predict_proba(justZScoreDifs)  # Creates list of probabilities that home team wins

    numCorrect = 0
    numWrong = 0
    allGames = []

    for i in range(len(probPredictions)):

        winProbability = probPredictions[i][1]
        homeTeam = withoutNums.iloc[i, 0]
        awayTeam = withoutNums.iloc[i, 1]
        date = withoutNums.iloc[i, 10]

        currentGameWithPred = [date, homeTeam, awayTeam, winProbability]

        allGames.append(currentGameWithPred)

        # Creates dataframe that holds all games info and predictions
        predictionsDF = pd.DataFrame(
            allGames,
            columns=['Date', 'Home', 'Away', 'Home Team Win Probability']
        )

        setCurrentWorkingDirectory('Data')
        predictionsDF.to_csv(outputFilename)  # Saves game info with predictions in data folder as csv file

        value = withoutNums.iloc[i,9]
        if value == predictions[i]:
            numCorrect += 1
        else :
            numWrong += 1

    print('Accuracy:')
    print((numCorrect)/(numCorrect+numWrong))  # Prints accuracy of model in predicting games


# Generates probability predictions over specified range of games exports them to a csv with game info
def makePastPredictions(startYear, startMonth, startDay, endYear, endMonth, endDay, season, startDateOfSeason,
                       gameDataFilename='gamesWithInfo.csv', outputFilename='predictions.csv'):

    # Obtains info for range of games
    getTrainingSetCSV(startYear, startMonth, startDay, endYear, endMonth, endDay, season, startDateOfSeason,
                          gameDataFilename)
    # Create probabilities for range of games
    getPredictionsCSV(gameDataFilename, outputFilename)


# start date (yyyy, m, d) (must be at least three days after start of season), end date (yyyy, m, d)
# season(yyyy-yy), start date of season (mm/dd/yyyy)

# EDIT THIS BASED ON REQUIRED SEASON
makePastPredictions(2019, 10, 28, 2019, 11, 3, '2019-20', '10/22/2019',
                    'gamesWithInfo.csv', 'predictions.csv')

# 2018 -19 NBA Season
# makePastPredictions(2018, 10, 27, 2019, 2, 10, '2018-19', '10/16/2018',
#                     'gamesWithInfo.csv', 'predictions.csv')

# 2019 -20 NBA Season
# makePastPredictions(2019, 10, 28, 2020, 10, 5, '2019-20', '10/22/2019',
#                     'gamesWithInfo.csv', 'predictions.csv')

# 2020 -21 NBA Season
# makePastPredictions(2020, 12, 28, 2021, 7, 15, '2019-20', '10/22/2019',
#                     'gamesWithInfo.csv', 'predictions.csv')