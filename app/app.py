import os
import random
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

TICKET_PRICES = {
    'Bilet 20 minutowy': 4,
    'Bilet 60 minutowy': 6,
    'Bilet 24 godzinny': 10,
    'Bilet 72 godzinny': 25
}

paper_state = 3

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

@app.route('/pay', methods=['POST'])
def pay():
    global paper_state
    data = request.get_json()
    total_amount = data.get('totalAmount')
    payment_method = data.get('paymentMethod')

    if paper_state <= 0:
        return jsonify({'success': False, 'message': 'Brak papieru. Proszę wymienić papier.'}), 400

    ticket_filename = f"Bilet-KrakTrans-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    ticket_path = os.path.join(os.getcwd(), ticket_filename)

    ticket_content = f"Krak-Trans\n_________________________\nData: {datetime.now().strftime('%Y-%m-%d')}\nGodzina: {datetime.now().strftime('%H:%M:%S')}\nTyp biletu: {data.get('ticketType')}\nUlga: {data.get('discountLabel')}\nPłatność: {'Karta' if payment_method == 'card' else 'Gotówka'}"
    with open(ticket_path, 'w', encoding='utf-8') as file:
        file.write(ticket_content)
    
    paper_state -= 1

    return jsonify({'success': True, 'message': 'Płatność zaakceptowana', 'ticketFilename': ticket_filename, 'paperState': paper_state})

@app.route('/download_ticket/<filename>', methods=['GET'])
def download_ticket(filename):
    ticket_path = os.path.join(os.getcwd(), filename)
    return send_file(ticket_path, as_attachment=True)

@app.route('/replace_paper', methods=['POST'])
def replace_paper():
    global paper_state
    paper_state = 3
    return jsonify({'success': True, 'paperState': paper_state})

if __name__ == "__main__":
    app.run(debug=True)
