import random
from flask import Flask, render_template, request, jsonify

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

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    data = request.get_json()
    ticket_type = data.get('ticketType')
    discount_type = data.get('discountType')
    
    if ticket_type not in TICKET_PRICES:
        return jsonify({'error': 'Nieprawidłowy typ biletu'}), 400

    ticket_price = TICKET_PRICES[ticket_type]
    if discount_type == 'reduced':
        ticket_price *= 0.5

    discount_label = 'Ulgowy' if discount_type == 'reduced' else 'Normalny'
    return jsonify({
        'ticketType': ticket_type,
        'discountLabel': discount_label,
        'ticketPrice': ticket_price
    })

@app.route('/remove_ticket', methods=['POST'])
def remove_ticket():
    data = request.get_json()
    ticket_price = data.get('ticketPrice')
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True)

