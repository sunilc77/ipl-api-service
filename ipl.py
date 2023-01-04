import numpy as np
import pandas as pd
from flask import json
matches = pd.read_csv('C:/Users/sunil/Downloads/CampusX/IPL_Matches_2008_2022 - IPL_Matches_2008_2022.csv')


# print(macthes.head(2))

def teamsAPI():
    teams = list(matches['Team1'].unique())
    team_dict = {'teams': teams}
    return team_dict


def teamVteamAPI(team1, team2):
    valid_teams = list(matches['Team1'].unique())
    if team1 in valid_teams and team2 in valid_teams:
        team_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team2'] == team1) & (matches['Team1'] == team2)]
        total_matches = team_df.shape[0]
        matches_won_team1 = team_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = team_df['WinningTeam'].value_counts()[team2]
        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
        'total_matches': str(total_matches),
         team1: str(matches_won_team1),
         team2: str(matches_won_team2),
        'draws': str(draws)
        }
        return response
    else:
        return {'message':'invalid team name'}