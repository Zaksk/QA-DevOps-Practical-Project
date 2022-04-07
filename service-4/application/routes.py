from application import app
from flask import Flask, request, Response
from random import choice

@app.route('/get_food', methods = ['POST'])
def food():
    picks_data = request.get_json()
    country_name = picks_data["Country"]
    prep_time = picks_data["Prep time"]
    food_dict = {"Morocco": {'20':['Couscous Cakes','Shakshuka','Zaalouk'],'30':['Moroccan Chickpea Stew','Moroccan Lentil Soup','adlkad'],'40':['Moroccan Chicken','Steamy Tagine','Chicken Couscous Salad']},
                "Italy":{'20':'Bruschetta Chicken Pasta','20':'Pot Tomato Basil Pasta','20':'Spaghetti & Chicken Meatball','30':'adlkad','30':'adlkad','30':'adlkad','40':'adlkad','40':'adlkad','40':'adlkad'}, 
                "Greek":{'20':'adlkad','20':'adlkad','20':'adlkad','30':'adlkad','30':'adlkad','30':'adlkad','40':'adlkad','40':'adlkad','40':'adlkad'},
                "Albania":{'20':'adlkad','20':'adlkad','20':'adlkad','30':'adlkad','30':'adlkad','30':'adlkad','40':'adlkad','40':'adlkad','40':'adlkad'}}
    return choice(food_dict[country_name][prep_time])


