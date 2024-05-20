import random
from flask import Flask, render_template

app = Flask(__name__)

TICKET_PRICES = {
    'Bilet 20 minutowy': 4,
    'Bilet 60 minutowy': 6,
    'Bilet 24 godzinny': 10,
    'Bilet 72 godzinny': 25
}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()