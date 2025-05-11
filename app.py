from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is what comes after you stop making excuses.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it."
    "In the darkest moments we must focus on the light!"
]

@app.route('/')
def quote():
    return f"<h1>{random.choice(quotes)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

