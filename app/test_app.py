import unittest
from flask import json
from app import app, TICKET_PRICES

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
            'totalAmount': 10.00
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
    
    def test_update_payment(self):
        payment_data = {
            'amountPaid': 5.00
        }
        response = self.app.post('/update_payment', data=json.dumps(payment_data), content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data)
        self.assertTrue(data['success'])
        self.assertIn('amountPaid', data)
        self.assertEqual(data['amountPaid'], payment_data['amountPaid'])


if __name__ == '__main__':
    unittest.main()