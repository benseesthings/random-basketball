from fastapi import FastAPI
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from src.openai_client import OpenAiClient
from src.player import Player

app = FastAPI()

all_players = players.get_players()

@app.get("/player")
def get_player():
    p = Player()
    player = p.generate_random_player()
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    points = p.player_points(career)
    assists = p.player_assists(career)
    years = p.years_played(career)

    open_ai_client = OpenAiClient()
    ai_response = open_ai_client.make_request(player['full_name'])

    return {
        "player": player['full_name'],
        "points": points,
        "assists": assists,
        "years": years,
        "fun_fact": ai_response
            }