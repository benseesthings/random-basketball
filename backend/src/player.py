from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import random

def player_points(career) -> int:
    df = career.get_data_frames()[1].to_dict()
    return df['PTS'][0]

def player_assists(career) -> int:
    df = career.get_data_frames()[1].to_dict()
    return df['AST'][0]

def years_played(career) -> int:
    df = career.get_data_frames()[0]
    years_played = len(df)
    return years_played

def generate_random_player() -> dict:
    all_players = players.get_players()
    random_integer = random.randint(0, len(all_players))
    return all_players[random_integer]