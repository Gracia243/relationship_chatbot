import json
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from flask_cors import CORS


# Download necesary NLTK data
nltk.download("vader_lexicon")
nltk.download("punkt")
sia = SentimentIntensityAnalyzer()

# Load training data from JSON file
def load_training_data():
    with open("responses.json", "r", encoding="utf-8") as file:
        return json.load(file)["training_data"]

def load_urgent_words():
    with open("responses.json", "r", encoding="utf-8") as file:
        return json.load(file)["urgent_words"]

training_data = load_training_data()
urgent_words = load_urgent_words()

# Extract training phrases and labels dynamically
training_phrases = []
training_labels = []

for category, data in training_data.items():
    if "training_phrases" in data:
        training_phrases.extend(data["training_phrases"])
        training_labels.extend([category]* len(data["training_phrases"]))

# Convert text to vectors for matching
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_phrases)

# Flask API setup
app = Flask(__name__)
CORS(app) # Enable CORS for fronted communication

# Function to analyse sentiment
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    compound = sentiment['compound']

    # Check if urgent words are present
    if any(word in text.lower() for word in urgent_words):
        return "urgent"

    # Classify sentiment
    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"


# Function to match user input to a category
def get_best_match(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, X_train)
    best_match_idx = np.argmax(similarities)

    if similarities[0][best_match_idx] > 0.7: # Basic threshold
        return training_labels[best_match_idx]
    return "default"

# Function generate a chatbot response
def get_response(user_input):
    sentiment = analyze_sentiment(user_input)
    category = get_best_match(user_input)

    # Check for urgent situations
    if sentiment == "urgent" or category == "domestic_violence":
        return random.choice(training_data["domestic_violence"]["responses"])

    # Seed random based on input to ensure consistency for the same question
    random.seed(hash(user_input))
    response = random.choice(training_data[category]["responses"])


    # Adjust response based on sentiment
    if sentiment == "negative":
        response += " I can see this is tough for you. You're not alone."
    elif sentiment == "positive":
        response += " That's great! Keep going in the right direction."

    # Debbuging output
    print(f"User Input: {user_input} | Category: {category} | Sentiment: {sentiment} | Response: {response}")
    
    return response

# API Endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    response = get_response(user_input)

    return jsonify({"response": response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
