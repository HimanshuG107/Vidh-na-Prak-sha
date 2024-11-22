import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from routes.iot_routes import iot_bp
from shared.utils.db_utils import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/iot_for_smart_homes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(iot_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
