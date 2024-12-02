from shared.utils.db_utils import db
from datetime import datetime
 
class Device(db.Model):
    __tablename__ = 'device'

    house_id = db.Column(db.Integer, db.ForeignKey('house.house_id'), nullable = False)
    device_id = db.Column(db.Integer, primary_key = True)
    device_name = db.Column(db.String(50), nullable = False)
    device_type = db.Column(db.String(50), nullable = False)
    device_status = db.Column(db.Integer, nullable = False)