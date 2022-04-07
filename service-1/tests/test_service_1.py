from flask import url_for
from flask_testing import TestCase
from datetime import date
import requests_mock
import pytest
# import the app's classes and objects
from application import app, db
from application.models import Foods

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                DEBUG=True,
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test event
        sample1 = Foods(country_name="Morocco", prep_time="up to 20", food_name="Harsha Bread", date_generated=date(2021, 6, 3))

        # save event to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
  
    def test_home_get(self):
        # mock values
        country = "Italy"
        food = "Spaghetti Bolognese"
        time = "up to 30"
        with requests_mock.Mocker() as m:
            m.get("http://event_generator_service-2:5000/get_country", text=country)
            m.get("http://event_generator_service-3:5000/get_time", text=time)
            m.post("http://event_generator_service-4:5000/get_food", text=food)
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Morocco', response.data)
            self.assertIn(b'Italy', response.data)

