from application import db

class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(50))
    country_name = db.Column(db.String(50))
    prep_time = db.Column(db.String(20))
    date_generated = db.Column(db.DateTime)
    def __str__(self):
        return f"You won {self.food_name}: From {self.country} and it takes {self.prep_time} minutes to prepare"