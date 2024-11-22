from shared.utils.db_utils import db

class user(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password_hash = db.Column(db.String(255), nullable = False)