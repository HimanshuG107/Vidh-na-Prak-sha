from shared.utils.db_utils import db

class ownes(db.Model):
        __tablename__ = 'ownes'

        id = db.Column(db.Integer, primary_key = True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
        device_id = db.Column(db.Integer, db.ForeignKey('device.device_id'), nullable = False)

