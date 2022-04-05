from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Events
import requests
from datetime import date


# home route
@app.route('/', methods = ['GET'])
def home():
    country_name = requests.get('http://service-2:5000/get_country')
    prep_time = requests.get('http://service-3:5000/get_time')
    food_name = requests.post('http://service-4:5000/get_food', json = {"Country": country_name.text, "Prep time": prep_time.text})
    new_food = Foods(event_name = country_name.text, prep_time = prep_time.text, food_name = food_name.text, date_generated = date.today())
    db.session.add(food)
    db.session.commit()
    past5 = Foods.query.order_by(Foods.id.desc()).limit(5).all()
    return render_template('index.html', food = food, past5 = past5)

@app.route('/history', methods=['GET'])
def history():
    foods_history = Foods.query.all()
    return render_template('history.html', foods_history = foods_history)
