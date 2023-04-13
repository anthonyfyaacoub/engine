
from flask import Blueprint, request, jsonify
#import generate_recommendations
from .recommendation_model import generate_recommendations
import openai
import json
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    input_data = int(data.get('input', ''))

    try:
        recommendations = generate_recommendations(input_data)
    except Exception as e:
        print(e)
        return jsonify({'error': "User not Found"}), 400

    return jsonify({
        'recommendations': recommendations
    })


@main.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data or "history" not in data:
        return jsonify({"error": "Message or history not provided"}), 400

    message = data["message"]
    history = data["history"]
    games = pd.read_pickle(r'backend-engine-main\recommendation_app\data\recommendations.txt')
    games = json.loads(r'backend-engine-main\recommendation_app\data\recommendations.json')
    games_str = ', '.join(games)

    # Preprogrammed context
    context = f"You are an expert in videogames and have vast knowledge about the following games: {games_str}. Your next answer should only say Hello! Would you like to know more about these games?"

    # Combine the context with the user's message
    prompt = f"{context}\n{history}\nUser: {message}\nExpert: "

    # Interact with the GPT-3.5 API
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    chatbot_response = response.choices[0].text.strip()
    return jsonify({"response": chatbot_response})
