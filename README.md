# Random Basketball Player

A simple FastAPI backend that returns random NBA players using [nba_api](https://github.com/swar/nba_api). I did this because I
wanted to get comfortable with using OpenAI's APIs as well as some other 
stuff, including wikipedia API. 

In order to run this correctly you'll need an OpenAI API key, which is not free. If you don't have one, 
it will just not serve the fun fact portion. 

## Setup

### Clone & Enter Project
```bash
git clone https://github.com/yourname/RandomBasketballPlayer.git
cd RandomBasketballPlayer/backend
```


## In backend
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

## In Frontend
```bash
npm install
```

```bash
npm start
```

Hit the button on the screen to receive a player. 