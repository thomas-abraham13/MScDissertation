Predicts NBA Regular Season Games Using a Logistic Regression Model in Python

# Model
The model uses eight factors scraped from stats.nba.com to predict the result of an NBA game. Each stat is adjusted to per 100 possessions to ensure pace has no impact on the predictions.

* Home Team
* Win Percentage
* Rebounds
* Turnovers
* Plus Minus
* Offensive Rating
* Defensive Rating
* True Shooting Percentage

# Run before execution:
pip3 install -r requirements.txt


# Generate Daily Predictions for Games:
1. Open nbaPredict.py

2. Edit the call to makeInterpretPrediction with desired date of games, season, and the start date of the season



3. Run the program either through the terminal or an IDE


4. Outcomes are outputted as the percent chance that the home team will beat the away team

# Generate Past Predicitons for Analysis:
1. Open makePastPredictions.py

2. Edit the call to makePastPredictions with required start date, end date, season, start date of the season, and output

NOTE: The start date should be at least three days after the season begins

3. Run the program either through the terminal or an IDE

4. Two CSV files will be saved in the Data folder. One holds the gameData and the other holds the predictions for the games.

# Accuracy Information:

# Confusion Matrix:
