from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "🌟 Be your own light.",
    "🔥 Discipline beats motivation.",
    "💡 Small steps every day lead to big change.",
    "🚀 Dream big. Start small. Act now.",
    "🧠 Your mind is your greatest weapon.",
    "⏳ Consistency creates confidence.",
    "🌱 Growth begins outside your comfort zone.",
    "⚡ Focus on progress, not perfection.",
    "🛠️ Build yourself before you build your dreams.",
    "🌈 You become what you repeatedly think."
]

@app.route('/')
def quote():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Daily Inspiration</title>
        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: white;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.15);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                text-align: center;
                max-width: 600px;
                backdrop-filter: blur(10px);
            }}
            h1 {{
                font-size: 2rem;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 0.9rem;
                opacity: 0.8;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{random.choice(quotes)}</h1>
            <p>🔄 Refresh to get a new quote</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

