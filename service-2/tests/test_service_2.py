from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
# import the app's classes and objects
from application import app

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_country(self):
       with patch('random.choice') as r:
           r.return_value = "Lebanon"
           response = self.client.get(url_for('country'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'Lebanon', response.data)