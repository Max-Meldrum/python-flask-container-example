import unittest
from api.app import app


class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user_status(self):
        result = self.app.get('/api/user')
        self.assertEqual(result.status_code, 200)
