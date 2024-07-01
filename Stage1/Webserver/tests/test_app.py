import unittest
from unittest.mock import patch
from app import app, get_location_and_temperature

class TestHelloEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.get_location_and_temperature')
    def test_hello_endpoint_with_visitor_name(self, mock_get_location_and_temperature):
        mock_get_location_and_temperature.return_value = {"city": "Nairobi", "temperature": 20}
        response = self.app.get('/api/hello?visitor_name=John')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"greeting": "Hello, John!, the temperature is 20 degrees Celsius in Nairobi"', response.data)

    @patch('app.get_location_and_temperature')
    def test_hello_endpoint_without_visitor_name(self, mock_get_location_and_temperature):
        mock_get_location_and_temperature.return_value = {"city": "Nairobi", "temperature": 20}
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"greeting": "Hello, Visitor!, the temperature is 20 degrees Celsius in Nairobi"', response.data)

    @patch('app.get_location_and_temperature')
    def test_hello_endpoint_with_different_location_and_temperature(self, mock_get_location_and_temperature):
        mock_get_location_and_temperature.return_value = {"city": "London", "temperature": 15}
        response = self.app.get('/api/hello?visitor_name=Jane')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"greeting": "Hello, Jane!, the temperature is 15 degrees Celsius in London"', response.data)

    def test_hello_endpoint_returns_json(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()
