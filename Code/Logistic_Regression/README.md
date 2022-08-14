# Model
The model uses eight factors scraped from stats.nba.com to predict the result of an NBA game. Each stat is adjusted to per 100 possessions to ensure pace has no impact on the predictions.

* Home Team (Home Court Advantage)
* Win Percentage
* Rebounds
* Turnovers
* Plus Minus
* Offensive Rating
* Defensive Rating
* True Shooting Percentage

## Run before Execution of Models:
pip3 install -r requirements.txt

## Generate Daily Predictions for Games:
1. Open nbaPredict.py

2. Edit the call to makeInterpretPrediction with desired date of games, season, and the start date of the season

![image](https://user-images.githubusercontent.com/29597130/184464636-70bce8c4-d107-40eb-b081-eec9cc4c860b.png)

3. Run the program either through the terminal or an IDE

4. Outcomes are displayed as the percent chance that the home team will beat the away team

## Generate Past Predicitons for Analysis:
1. Open makePastPredictions.py

2. Edit the call to makePastPredictions with required start date, end date, season, start date of the season, and output

NOTE: The start date should be at least three days after the season begins

![image](https://user-images.githubusercontent.com/29597130/184464663-6ac00692-cb37-4994-a5ed-8b1eb2d66066.png)

3. Run the program either through the terminal or an IDE

4. Two CSV files will be saved in the Data folder. One holds the gameData and the other holds the predictions for the games.

## Accuracy Information:

![image](https://user-images.githubusercontent.com/29597130/184500263-b221750c-b278-4680-b42c-c4de1ed81534.png)

## Confusion Matrix:

![image](https://user-images.githubusercontent.com/29597130/184464723-e93cf21a-278a-40fa-84cc-3a763c5c8ee9.png)