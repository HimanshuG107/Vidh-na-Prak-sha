import sys, os
sys.path.append(os.getcwd())
sys.path.append(r"D:/iot_for_smart_homes_data")

from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate

# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/iot_for_smart_homes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

from models import alerts_model
from models import device_model
from models import location_model
from models import house_model
from models import sensor_model
from models import sensorData_model
from models import user_model
from models import ownes_model
from models import gives_model
