from application import app
from flask import Flask, request, Response
import random

@app.route('/get_country', methods=['GET'])
def country():
    country_name = random.choice(["Morocco","Italy","Lebanon",])
    return Response(country_name, mimetype='text/plain')