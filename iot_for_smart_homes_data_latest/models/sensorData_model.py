from datetime import datetime
from shared.utils.db_utils import db

class SensorData(db.Model):
    __tablename__ = 'sensor_data'

    sensor_data_id = db.Column(db.Integer, primary_key = True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'), nullable = False)
    data_value = db.Column(db.Integer, nullable = False)
    sensor_time = db.Column(db.DateTime,  default = datetime.utcnow)