from shared.utils.db_utils import db


class Sensor(db.Model):
    __tablename__ = 'sensor'

    sensor_id = db.Column(db.Integer, primary_key = True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.device_id'), nullable = False)
    sensor_type = db.Column(db.String(50), nullable = False)
    sensor_status = db.Column(db.Boolean, nullable = False)
    