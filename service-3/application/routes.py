from application import app
from flask import Flask, request, Response
import random

@app.route('/get_time', methods=['GET'])
def time():
    prep_time = random.choice(["20", "30", "40"])
    return Response(prep_time, mimetype='text/plain')