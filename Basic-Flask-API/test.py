import unittest
from app import app

class Test(unittest.TestCase):
    def setUp(self):
        '''setting up the test client'''
        self.client = app.test_client()
        self.client.testing = True

    def testhome(self):
        '''Testing the Home route'''
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{'message':"Welcome to the Home page"})



# Test Client: Uses Flask's test_client() to simulate HTTP requests.

# Assertions: Check both status codes and response data for accuracy.