import unittest
from unittest.mock import patch
from app import app

class TestProductionEndpoints(unittest.TestCase):
    @patch('services.productionService.find_all')
    def test_get_all_productions(self, mock_find_all):
        mock_find_all.return_value = [{"id": 1, "product_id": 1, "quantity": 100}]

        with app.test_client() as client:
            response = client.get('/productions')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['quantity'], 100)

    @patch('services.productionService.save')
    def test_save_production(self, mock_save):
        mock_save.return_value = {"id": 2, "product_id": 2, "quantity": 50}

        with app.test_client() as client:
            response = client.post('/productions', json={"product_id": 2, "quantity": 50})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['quantity'], 50)

    @patch('services.productionService.find_by_id')
    def test_get_production_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        with app.test_client() as client:
            response = client.get('/productions/999')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
