from shared.utils.db_utils import db

class Location(db.Model):
    __tablename__ = 'location'

    location_id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(30), nullable = False)
    city = db.Column(db.String(50), nullable = False)
    zipcode = db.Column(db.String(20), nullable = False)
