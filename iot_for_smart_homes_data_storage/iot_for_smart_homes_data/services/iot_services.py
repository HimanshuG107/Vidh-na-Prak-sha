from models.user_model import user
from models.location_model import Location
from models.house_model import House
from models.device_model import Device
from models.sensor_model import Sensor
from models.sensorData_model import SensorData
from models.alerts_model import Alerts
from models.gives_model import gives
from models.ownes_model import ownes
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash

class IotService:
    @staticmethod
    def create_user(username, email, password, full_name, bio):
        hashed_password = generate_password_hash(password)
        new_user = user(username=username, email=email, password_hash=hashed_password, full_name=full_name, bio=bio)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def get_user_by_username(username):
        return user.query.filter_by(username=username).first()

    @staticmethod
    def get_user(user_id):
        return user.query.filter_by(user_id = user_id).first()

    @staticmethod
    def get_all_users():
        return user.query.all()

    @staticmethod
    def verify_user(username, password):
        user = user.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None
    
    @staticmethod
    def add_location(location_id, state, city, zip):
        new_location = Location(location_id=location_id, state=state, city=city, zipcode=zip)
        db.session.add(new_location)
        db.session.commit()

        return new_location

    @staticmethod
    def add_house(house_id, user_id, location_id, room_id, house_no):
        user = user.query.filter_by(user_id=user_id).first()
        location = Location.query.filter_by(location_id=location_id).first()
        if user and location:
            new_house = House(house_id=house_id, user_id=user_id, location_id=location_id, room_id=room_id, house_no=house_no)
            db.session.add(new_house)
            db.session.commit(new_house)
            return new_house
        return None
    
    @staticmethod
    def get_location_by_location_id(location_id):
        return Location.query.filter_by(location_id=location_id).first()

    @staticmethod
    def get_all_locations():
        return Location.query.all()
    
    @staticmethod
    def get_house_by_house_id(house_id):
        return House.query.filter_by(house_id=house_id).first()

    @staticmethod
    def get_all_houses():
        return House.query.all()
    
    @staticmethod
    def add_device(device_id, house_id, device_name, device_type, device_status):
        house = House.query.filter_by(house_id=house_id).first()
        if house:
            new_device = Device(device_id=device_id, house_id=house_id, device_name=device_name, device_type=device_type, device_status=device_status)
            db.session.add(new_device)
            db.session.commit()
            return new_device
        return None
    
    def toggle_device(device_id):
        device = Device.query.filter_by(device_id=device_id).first()
        if device:
            device.sensor_status = not device.sensor_status
            db.session.commit()
            return None
        return None
    
    @staticmethod
    def add_sensor(sensor_id, device_id, sensor_type, sensor_status):
        device = Device.query.filter_by(device_id=device_id).first()
        if device:
            new_sensor = Sensor(sensor_id=sensor_id, device_id=device_id, sensor_type=sensor_type, sensor_status=sensor_status)
            db.session.add(new_sensor)
            db.session.commit()
            return new_sensor
        return None
    
    def toggle_sensor(sensor_id):
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            sensor.sensor_status = not sensor.sensor_status
            db.session.commit()
            return None
        return None
    
    @staticmethod
    def add_sensorData(sensorData_id, sensor_id, data_value):
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            new_sensorData = SensorData(sensorData_id=sensorData_id, sensor_id=sensor_id, data_value=data_value)
            db.session.add(new_sensorData)
            db.session.commit()
            return new_sensorData
        return None
    
    @staticmethod
    def get_device_by_device_id(device_id):
        return Device.query.filter_by(device_id=device_id).first()

    @staticmethod
    def get_all_devices():
        return Device.query.all()
    
    @staticmethod
    def get_sensor_by_sensor_id(sensor_id):
        return Sensor.query.filter_by(sensor_id=sensor_id).first()

    @staticmethod
    def get_all_sensors():
        return Sensor.query.all()
    
    @staticmethod
    def create_alert(alert_id, alert_time, alert_type, message, alert_status):
        new_alert = Alerts(alert_id=alert_id, alert_time=alert_time, alert_type=alert_type, message=message, alert_status=alert_status)
        db.session.add(new_alert)
        db.session.commit()
        return new_alert
    
    @staticmethod
    def create_gives_tuple(device_id, alert_id):
        device = Device.query.filter_by(device_id=device_id).first()
        if device:
            new_gives_tuple = gives(device_id=device_id, alert_id=alert_id)
            db.session.add(new_gives_tuple)
            db.commit()
            return new_gives_tuple
        return None

    @staticmethod
    def get_all_alerts():
        return Alerts.query.all()

    @staticmethod
    def turn_off_alert_by_alert_id(alert_id):
        alert = Alerts.query.filter_by(alert_id=alert_id).first()
        if alert:
            alert.alert_status = False
            db.session.commit()
            return None
        return None
    
    @staticmethod
    def get_alert_by_time_interval(start_time, end_time):
        return Alerts.query.filter(Alerts.alert_time >= start_time and Alerts.alert_time <= end_time).all()
           
    @staticmethod
    def create_ownes_tuple(user_id, device_id):
        user = user.query.filter_by(user_id).first()
        if user:
            new_ownes_tuple = ownes(user_id = user_id, device_id = device_id)
            db.session.add(new_ownes_tuple)
            db.sessionn.commit()
            return new_ownes_tuple
        return None
