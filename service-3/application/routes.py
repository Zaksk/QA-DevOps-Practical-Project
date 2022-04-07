from application import app
from flask import Flask, request, Response
import random

@app.route('/get_time', methods=['GET'])
def time():
    prep_time = random.choice(["up to 20","up to 30","up to 40","more than 50"])
    return Response(prep_time, mimetype='text/plain')