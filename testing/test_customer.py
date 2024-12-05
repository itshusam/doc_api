import unittest
from unittest.mock import patch
from app import app

class TestCustomerEndpoints(unittest.TestCase):
    @patch('services.customerService.find_all')
    def test_get_all_customers(self, mock_find_all):
        mock_find_all.return_value = [{"id": 1, "name": "Customer A"}]

        with app.test_client() as client:
            response = client.get('/customers')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['name'], "Customer A")

    @patch('services.customerService.save')
    def test_save_customer(self, mock_save):
        mock_save.return_value = {"id": 2, "name": "Customer B"}

        with app.test_client() as client:
            response = client.post('/customers', json={"name": "Customer B"})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['name'], "Customer B")

    @patch('services.customerService.find_by_id')
    def test_get_customer_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        with app.test_client() as client:
            response = client.get('/customers/999')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
