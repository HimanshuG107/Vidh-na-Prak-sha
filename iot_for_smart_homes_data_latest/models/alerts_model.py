from shared.utils.db_utils import db
from datetime import datetime

class Alerts(db.Model):
    __tablename__ = 'alert'

    alert_id = db.Column(db.Integer, primary_key = True)
    alert_time = db.Column(db.DateTime, default = datetime.utcnow)
    alert_type = db.Column(db.String(50), nullable = False)
    messege = db.Column(db.String(50), nullable = False)
    alert_status = db.Column(db.Boolean, nullable = False)

