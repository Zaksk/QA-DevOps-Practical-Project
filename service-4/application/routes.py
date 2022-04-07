from application import app
from flask import Flask, request, Response
from random import choice

@app.route('/get_food', methods = ['POST'])
def food():
    picks_data = request.get_json()
    country_name = picks_data["Country"]
    prep_time = picks_data["Prep time"]
    food_dict = {"Morocco": {'up to 20':['Harsha Bread','Shakshuka','Zaalouk'],'up to 30':['Moroccan Chickpea Stew','Moroccan Lentil Soup','Merguez Wrap'],'up to 40':['Harira','Grilled moroccan lamb chops','Tagine'],'more than 50':['Couscous','Bastilla','Seffa']},
    "Italy": {'up to 20':['Caesar Salad','Bruschette','Butterfly King Prawns'],'up to 30':['Spaghetti Bolognese','Pizza Margherita','Lasagna'],'up to 40':['Ravioli','Tiramisu','Sea Bass Al Forno'],'more than 50':['Risotto','Manzo Piccante','Calzone Carne Piccante']},
    "Lebanon": {'up to 20':['Batata Harra','Labneh','Hummus'],'up to 30':['Shawarma Wrap','Zaatar Bread','Lamb Kibbeh'],'up to 40':['Mixed Grill','Falafel','Kunefa'],'more than 50':['Maamoul','Namoura','Lebanese Chicken Rice']}}
    return choice(food_dict[country_name][prep_time])


