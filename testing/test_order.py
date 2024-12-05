import unittest
from unittest.mock import patch
from app import app

class TestOrderEndpoints(unittest.TestCase):
    @patch('services.orderService.find_all')
    def test_get_all_orders(self, mock_find_all):
        mock_find_all.return_value = [{"id": 1, "product_id": 1, "quantity": 10}]

        with app.test_client() as client:
            response = client.get('/orders')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['quantity'], 10)

    @patch('services.orderService.save')
    def test_save_order(self, mock_save):
        mock_save.return_value = {"id": 2, "product_id": 2, "quantity": 5}

        with app.test_client() as client:
            response = client.post('/orders', json={"product_id": 2, "quantity": 5})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['quantity'], 5)

    @patch('services.orderService.find_by_id')
    def test_get_order_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        with app.test_client() as client:
            response = client.get('/orders/999')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
