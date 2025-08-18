from fastapi import FastAPI
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from src import player as play

app = FastAPI()

all_players = players.get_players()

@app.get("/player")
def get_player():
    player = play.generate_random_player()
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    points = play.player_points(career)
    assists = play.player_assists(career)
    years = play.years_played(career)
    return {
        "player": player['full_name'],
        "points": points,
        "assists": assists,
        "years": years
            }