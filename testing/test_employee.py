import unittest
from unittest.mock import patch
from app import app

class TestEmployeeEndpoints(unittest.TestCase):
    @patch('services.employeeService.find_all')
    def test_get_all_employees(self, mock_find_all):
        mock_find_all.return_value = [{"id": 1, "name": "Employee A"}]

        with app.test_client() as client:
            response = client.get('/employees')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['name'], "Employee A")

    @patch('services.employeeService.save')
    def test_save_employee(self, mock_save):
        mock_save.return_value = {"id": 2, "name": "Employee B"}

        with app.test_client() as client:
            response = client.post('/employees', json={"name": "Employee B"})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['name'], "Employee B")

    @patch('services.employeeService.find_by_id')
    def test_get_employee_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        with app.test_client() as client:
            response = client.get('/employees/999')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
