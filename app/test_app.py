import unittest
from flask import json
from app import app, TICKET_PRICES
import os


class TestTicketMachineAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_ticket(self):
        ticket_data = {
            'ticketType': 'Bilet 20 minutowy',
            'discountType': 'normal'
        }
        response = self.app.post('/add_ticket', data=json.dumps(ticket_data), content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('ticketType', data)
        self.assertIn('discountLabel', data)
        self.assertIn('ticketPrice', data)
        self.assertEqual(data['ticketType'], ticket_data['ticketType'])
        self.assertEqual(data['discountLabel'], 'Normalny')
        self.assertEqual(data['ticketPrice'], TICKET_PRICES[ticket_data['ticketType']])

    def test_add_ticket_invalid_type(self):
        ticket_data = {
            'ticketType': 'Invalid Ticket',
            'discountType': 'normal'
        }
        response = self.app.post('/add_ticket', data=json.dumps(ticket_data), content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Nieprawidłowy typ biletu')

    def test_remove_ticket(self):
        ticket_data = {
            'ticketType': 'Bilet 20 minutowy',
            'ticketPrice': 4.00
        }
        response = self.app.post('/remove_ticket', data=json.dumps(ticket_data), content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data)
        self.assertTrue(data['success'])

    def test_pay(self):
        payment_data = {
            'totalAmount': 10.00,
            'ticketType': 'Bilet 20 minutowy',
            'discountLabel': 'Normalny',
            'paymentMethod': 'cash'
        }
        response = self.app.post('/pay', data=json.dumps(payment_data), content_type='application/json')
        data = json.loads(response.data)

        self.assertIn('success', data)
        self.assertIn('message', data)
        if data['success']:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], 'Płatność zaakceptowana')
        else:
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data['message'], 'Płatność odrzucona')

    def test_replace_paper(self):
        response = self.app.post('/replace_paper', content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data)
        self.assertTrue(data['success'])
        self.assertIn('paperState', data)
        self.assertEqual(data['paperState'], 3)

    def test_download_ticket(self):
        ticket_filename = 'test_ticket.txt'
        with open(ticket_filename, 'w', encoding='utf-8') as f:
            f.write("Test ticket content")

        response = self.app.get(f'/download_ticket/{ticket_filename}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/plain')
        self.assertEqual(response.headers['Content-Disposition'], f'attachment; filename={ticket_filename}')

        response.close()
        os.remove(ticket_filename)


if __name__ == '__main__':
    unittest.main()
