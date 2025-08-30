import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

from src.openai_client import make_request
from src.player import generate_random_player, years_played, player_assists, player_points

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

all_players = players.get_players()

@app.get("/player")
async def get_player():
    player = generate_random_player()
    wiki_thumb = await wikipedia_thumb(player['full_name'])
    player_id = player['id']
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    points = player_points(career)
    assists = player_assists(career)
    years = years_played(career)

    ai_response = make_request(player['full_name'])

    return {
        "player": player['full_name'],
        "points": points,
        "assists": assists,
        "years": years,
        "fun_fact": ai_response,
        "image_url": wiki_thumb
        }

async def wikipedia_thumb(name: str):
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": f"{name} basketball",  # bias search toward the player
        "gsrlimit": 1,
        "prop": "pageimages",
        "piprop": "thumbnail",
        "pithumbsize": 600,
        "format": "json",
    }
    headers = {"User-Agent": "RandomBasketballPlayer/1.0 (contact: you@example.com)"}
    async with httpx.AsyncClient(timeout=6, headers=headers) as c:
        r = await c.get("https://en.wikipedia.org/w/api.php", params=params)
        data = r.json()
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():                  # first (best) hit
            thumb = page.get("thumbnail")
            if thumb and "source" in thumb:
                return thumb["source"]
    return None