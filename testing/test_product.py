import unittest
from unittest.mock import patch
from app import app

class TestProductEndpoints(unittest.TestCase):
    @patch('services.productService.find_all')
    def test_get_all_products(self, mock_find_all):
        mock_find_all.return_value = [{"id": 1, "name": "Product A"}]

        with app.test_client() as client:
            response = client.get('/products')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['name'], "Product A")

    @patch('services.productService.save')
    def test_save_product(self, mock_save):
        mock_save.return_value = {"id": 2, "name": "Product B"}

        with app.test_client() as client:
            response = client.post('/products', json={"name": "Product B"})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['name'], "Product B")

    @patch('services.productService.find_by_id')
    def test_get_product_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        with app.test_client() as client:
            response = client.get('/products/999')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
