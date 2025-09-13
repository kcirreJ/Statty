from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
from google.genai import types
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('GEMINI_API_KEY')

app = Flask(__name__)
CORS(app)


@app.route('/')
def start():
    return 'running'

@app.route('/api/player_stats')
def get_player_stats():
    player_name = request.args.get('player_name', '').title()
    sport = request.args.get('sport', '').title()

    if not player_name or not sport:
        return jsonify({"error": "Player name and sport are required."}), 400

    try:

        client = genai.Client(api_key=api_key)

        grounding_tool = types.Tool(
                google_search=types.GoogleSearch()
                )

        config = types.GenerateContentConfig(
                tools=[grounding_tool]
                )

        prompt = (
                 f"Search for the stats from the most recent {sport} game, played by the player "
                 f"named {player_name}. Provide the data as plain text with the player's "
                 f"full name, team, and a 'stats' object containing key-value pairs "
                 f"For basketball, include stats like 'Points Per Game', 'Rebounds Per Game', and "
                 f"'Assists Per Game'. For soccer, include stats like 'Goals', 'Assists', 'Shots', and "
                 f"'Shots on Target'. Please format the response as a simple, human-readable text. Do "
                 f"not use any JSON formatting, or include other text / explanation. For Soccer, only "
                 f"provide results for players in top flight leagues from, England, Spain, Italy, Germany, "
                 f"Portugal, France, Netherlands, USA, and Turkey. For Basketball, only provide results "
                 f"for players in the NBA. Display names as shown on FOTMOB / ESPN profiles."
                )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[{"parts": [{"text": prompt}]}],
            config=config
        )

        stats_data = response.candidates[0].content.parts[0].text

        return jsonify(stats_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Failed to fetch data from the API. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True)
