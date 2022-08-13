# Execute: python getDailyMatchups.py
# Used to Display Probabilities for Daily NBA games

from nba_api.stats.endpoints import leaguegamelog, scoreboard
from teamIds import teams
from customHeaders import customHeaders

# Function to get you the games on a specified date (Home vs. Away)
# Enter a date in the format mm/dd/yyyy and season in the format yyyy-yy
def dailyMatchupsPast(date, season):

    # Obtains a list of teams who played on specified date
    dailyMatchups = leaguegamelog.LeagueGameLog(season=season, league_id='00', season_type_all_star='Regular Season', date_from_nullable=date,date_to_nullable=date, headers=customHeaders,timeout=60)
    dailyMatchupsDict = dailyMatchups.get_normalized_dict()
    listOfTeams = dailyMatchupsDict['LeagueGameLog']

    winLossList = []
    homeAwayDict = {}
    for i in range(0,len(listOfTeams),2):
        if '@' in listOfTeams[i]['MATCHUP']:  # @ indicates that the current team is away
            awayTeam = listOfTeams[i]['TEAM_NAME']
            homeTeam = listOfTeams[i+1]['TEAM_NAME']

            winLossList.append(listOfTeams[i+1]['WL'])  # Appends if the home team won or lost from list

        else:
            awayTeam = listOfTeams[i+1]['TEAM_NAME']
            homeTeam = listOfTeams[i]['TEAM_NAME']

            winLossList.append(listOfTeams[i]['WL'])  # Appends if the home team won or lost from list

        homeAwayDict.update({homeTeam:awayTeam})  # Adds current game to list of all games for that day

    matchupsResultCombined = [homeAwayDict, winLossList]  # Combines game results into one list
    return(matchupsResultCombined)


# Function to get you the games on a specified date
# Used for dates in the present or future
def dailyMatchupsPresent(date):

    # Gets all games that are set to occur on specified date
    dailyMatchups = scoreboard.Scoreboard(league_id='00', game_date=date, headers=customHeaders, timeout=120)
    dailyMatchupsDict = dailyMatchups.get_normalized_dict()
    listOfGames = dailyMatchupsDict['GameHeader']

    homeAwayDict = {}

    for game in listOfGames:  # Loops through each game for that date

        homeTeamID = game['HOME_TEAM_ID']

        for team, teamID in teams.items():  # Finds name of the home team with teamID
            if teamID == homeTeamID:
                homeTeamName = team

        awayTeamID = game['VISITOR_TEAM_ID']

        for team, teamID in teams.items():  # Finds name of the away team with teamID
            if teamID == awayTeamID:
                awayTeamName = team

        homeAwayDict.update({homeTeamName:awayTeamName})

    return homeAwayDict