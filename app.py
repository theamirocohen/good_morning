from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Pool of strings
quotes = [
    "yo yo bitch!",
    "you cant touch this!",
    "see you later alligator!",
    "continuous lunch!",
    "prometheus is the shit!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quote')
def get_quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)
