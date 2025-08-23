import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

class OpenAiClient:
    def make_request(self, player):
        response = client.responses.create(
            model="gpt-4o-mini",
            input=f"Give me a fun fact about this basketball player: {player}. Preferably the fact will"
                  f"not be related to basketball. Something from his personal life, funny or interesting. Please"
                  f"make this one sentence long."
        )

        return response.output_text

