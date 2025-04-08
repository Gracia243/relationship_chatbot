# Relationship Chatbot

A chatbot application designed to provide advice and support on relationship-related issues. Built with Flask for the backend and React for the frontend. The chatbot uses Natural Language Processing (NLP) techniques to analyze user input and respond accordingly.

## Features

- **Sentiment Analysis**: The bot can understand the sentiment behind the user's message (positive, neutral, or negative).
- **Intent Recognition**: Based on the user's input, the chatbot identifies common relationship issues and provides personalized responses.
- **Support for Multiple Topics**: Handles a variety of relationship topics including communication, trust, conflict, love languages, and more.
- **User-Friendly Interface**: A clean and responsive UI designed to simulate an SMS conversation.

## Tech Stack

- **Backend**: 
  - Python
  - Flask
  - NLTK (Natural Language Toolkit) for sentiment analysis
  - scikit-learn for text vectorization and similarity matching
  - Flask-CORS for handling cross-origin requests

- **Frontend**:
  - React
  - Axios for making HTTP requests

## Installation

### Prerequisites:

- Python 3.6+
- Node.js (for frontend development)
- npm or yarn (for React frontend)

### Backend (Flask) Setup:

1. Clone this repository:
   ```bash
   git clone https://github.com/Gracia243/relationship-chatbot.git
   ```
2. Navigate to the backend directory:
   ```bash
   cd relationship-chatbot/backend
   ```
3. Create a virtual environment and activate it:
    - On Windows :
   ```bash
   python -m venv venv
    venv\Scripts\activate
   ```
   - On Mac/Linux:
   ```bash
   python3 -m venv venv
    source venv/bin/activate
   ```
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```bash
   flask run
   ```

### Frontend (React) Setup:

1. Navigate to the frontend directory:
   ```bash
   cd relationship-chatbot/frontend
   ```
2. Install the required dependencies:
   ```bash
   npm install
   ```
3. Run the React development server:
   ```bash
   npm start
   ```

   The frontend application will be available at
   `http://localhost:3000/`

## Usage

- Open the React app in your browser.
- Type a message in the input box and click "Send."
- The chatbot will analyze your message, understand the sentiment, and provide a relevant response based on predefined categories (communication, trust, conflict, etc.).

## File structure
```plaintext
relationship-chatbot/
│
├── backend/                # Flask API files
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Backend dependencies
│   ├── responses.json     # JSON file containing responses and training data
│   └── ...
│
├── frontend/               # React app files
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── ChatBot.js      # Chatbot component
│   │   └── ...
│   ├── public/
│   │   └── index.html
│   ├── package.json        # Frontend dependencies
│   └── ...
└── README.md               # This file
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. You can also open issues to report bugs or suggest new features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- **NLTK:** Used for sentiment analysis.
- **Flask:** Web framework for the backend.
- **React:** Frontend framework for creating the interactive chatbot interface.
- **scikit-learn:** Used for text vectorization and similarity comparison.

