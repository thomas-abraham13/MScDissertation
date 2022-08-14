# Elo Algorithm

### The directories present consist of python code and datasets required to predict the final seeds of NBA teams for a regular season

NOTE: The test data and results present relate to the 2018-2019 NBA Season

## Directories

1) dataset :
    Contains the related datasets pertaining to varous NBA seasons 

2) main :
    Contains the main modules related to the development of the final eloRun.py file

    In order to view the prediction rate, run the following command in the main directory;

        python train_test.py

3) plots:
    Contains the graphs plotted to gain an understanding of player strength and prediction accuracy

4) scraping:
    Contains the python scripts used to scrape the required data directly from stats.nba.com using the package selenium

Execute: python eloRun.py

The above command will run the Elo Algorithm on data from the 2018-19 NBA Regular season and produce a prediction for the playoffs.