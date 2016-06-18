import unittest
from api.app import app


class UserTest(unittest.TestCase):
    """Unit tests for the User resource, ensuring that everything is
    correct."""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user_root(self):
        result = self.app.get('/api/user')
        self.assertEqual(result.status_code, 200)
