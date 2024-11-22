from shared.utils.db_utils import db

class gives(db.Model):
        __tablename__ = 'gives'

        id = db.Column(db.Integer, primary_key = True)
        device_id = db.Column(db.Integer, db.ForeignKey('device.device_id'), nullable = False)
        alert_id = db.Column(db.Integer, db.ForeignKey('alerts.alert_id'), nullable = False)
