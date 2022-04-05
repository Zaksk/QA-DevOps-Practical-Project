from application import app
from flask import Flask, request, Response

@app.route('/get_food', methods = ['POST'])
def effect():
    picks_data = request.get_json()
    country_name = picks_data["Country"]
    prep_time = picks_data["Prep time"]

    


