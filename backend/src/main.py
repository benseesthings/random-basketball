from fastapi import FastAPI
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import random

DB_PATH = "data/nba.sqlite"

app = FastAPI()

@app.get("/player")
def get_player():
    all_players = players.get_players()
    random_integer = random.randint(0, len(all_players))
    return all_players[random_integer]["full_name"]
