import unittest
from api import app


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status(self):
        result = self.app.get('/user')
        self.assertEqual(result.status_code, 200)
