from shared.utils.db_utils import db

class House(db.Model):
    __tablename__ = 'house'

    house_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'), nullable = False)
    room_id = db.Column(db.Integer, unique = True, nullable = False)
    house_no = db.Column(db.Integer, nullable = False)
