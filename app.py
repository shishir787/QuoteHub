from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧  
 "Be yourself;  
  everyone else  
  is already taken."  
        — Oscar Wilde  
✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧
"
]

@app.route('/')
def quote():
    return f"<h1>{random.choice(quotes)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

