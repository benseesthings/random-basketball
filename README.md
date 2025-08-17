# Random Basketball Player

A simple FastAPI backend that returns random NBA players using [nba_api](https://github.com/swar/nba_api).

## Setup

### Clone & Enter Project
```bash
git clone https://github.com/yourname/RandomBasketballPlayer.git
cd RandomBasketballPlayer/backend
```

### Setup Virtual Env
```bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.\.venv\Scripts\activate    # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the server
```bash
uvicorn src.main:app --reload --port 8080
```

The backend is live at http://127.0.0.1:8080

Hit ```/player``` to receive one. 