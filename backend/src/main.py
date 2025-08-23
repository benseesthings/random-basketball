from fastapi import FastAPI
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

from src.openai_client import make_request
from src.player import generate_random_player, years_played, player_assists, player_points

app = FastAPI()

all_players = players.get_players()

@app.get("/player")
def get_player():
    player = generate_random_player()
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    points = player_points(career)
    assists = player_assists(career)
    years = years_played(career)

    ai_response = make_request(player['full_name'])

    return {
        "player": player['full_name'],
        "points": points,
        "assists": assists,
        "years": years,
        "fun_fact": ai_response
            }