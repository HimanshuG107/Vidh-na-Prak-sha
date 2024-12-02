from flask import Blueprint
from controller.UserController import UserController
from controller.AlertsController import AlertsController
from controller.DeviceController import DeviceController
from controller.GivesController import GivesController
from controller.HouseController import HouseController
from controller.LocationController import LocationController
from controller.OwnesController import OwnesController
from controller.SensorController import SensorController 

iot_bp = Blueprint('iot_bp', __name__)


@iot_bp.route('/api/user/create', methods = ['POST'])
def create_user():
    return UserController.create_user()

@iot_bp.route('/api/user', methods = ['GET'])
def get_all_users():
    return UserController.get_all_users()

@iot_bp.route('/api/user/<name>', methods = ['GET'])
def get_user_by_name(name):
        return UserController.get_user_by_username(name)

@iot_bp.route('/api/user/login', methods = ['POST'])
def user_login():
    return UserController.user_login()

@iot_bp.route('/api/user/<int:user_id>', methods = ['GET'])
def get_user(user_id):
        return UserController.get_user(user_id)

@iot_bp.route('/api/device/add_device', methods = ['POST'])
def add_device():
        return DeviceController.add_device()

@iot_bp.route('/api/device', methods = ['GET'])
def get_all_devices():
    return DeviceController.get_all_devices()

@iot_bp.route('/api/alert', methods = ['POST'])
def create_alert():
        return AlertsController.create_alert() 

@iot_bp.route('/api/alert/get_all_alerts', methods = ['GET'])
def get_all_alerts():
        return AlertsController.get_all_alerts()

@iot_bp.route('/api/alert/turn_off_alert_by_alert_id/<int:alert_id>', methods = ['PUT'])
def turn_off_alert_by_alert_id(alert_id):
        return AlertsController.turn_off_alert_by_alert_id(alert_id) 

@iot_bp.route('/api/alert/get_alerts_by_time_interval', methods = ['GET'])
def get_alerts_by_time_interval():
        return AlertsController.get_alerts_by_time_interval() 

@iot_bp.route('/api/device/<int:device_id>', methods = ['GET'])
def get_device_by_device_id(device_id):
        return DeviceController.get_device_by_device_id(device_id) 

@iot_bp.route('/api/device/get_information_of_devices/<int:house_id>', methods = ['GET'])
def get_information_of_devices(house_id):
        return DeviceController.get_information_of_devices(house_id) 



@iot_bp.route('/api/device/toggle_device/<int:device_id>', methods = ['PUT'])
def toggle_device(device_id):
        return DeviceController.toggle_device(device_id) 

@iot_bp.route('/api/gives/create_gives_tuple', methods = ['POST'])
def create_gives_tuple():
        return GivesController.create_gives_tuple() 

@iot_bp.route('/api/house/add_house', methods = ['POST'])
def add_house():
        return HouseController.add_house()

@iot_bp.route('/api/house/get_all_houses', methods = ['GET'])
def get_all_houses():
        return HouseController.get_all_houses()

@iot_bp.route('/api/house/get_house_by_house_id/<int:house_id>', methods = ['GET'])
def get_house_by_house_id(house_id):
        return HouseController.get_house_by_house_id(house_id)

@iot_bp.route('/api/location/add_location', methods = ['POST'])
def add_location():
        return LocationController.add_location()

@iot_bp.route('/api/location/get_all_locations', methods = ['GET'])
def get_all_locations():
        return LocationController.get_all_locations()

@iot_bp.route('/api/location/get_location_by_location_id/<int:location_id>', methods = ['GET'])
def get_location_by_location_id(location_id):
        return LocationController.get_location_by_location_id(location_id)

@iot_bp.route('/api/ownes/create_ownes_tuple', methods = ['POST'])
def create_ownes_tuple():
        return OwnesController.create_ownes_tuple()


@iot_bp.route('/api/sensor/add_sensor', methods = ['POST'])
def add_sensor():
        return SensorController.add_sensor()


@iot_bp.route('/api/sensor/toggle_sensor/<int:sensor_id>', methods = ['PUT'])
def toggle_sensor(sensor_id):
        return SensorController.toggle_sensor(sensor_id)


@iot_bp.route('/api/sensor/get_all_sensors', methods = ['GET'])
def get_all_sensors():
        return SensorController.get_all_sensors() 

@iot_bp.route('/api/sensor/get_sensor_by_sensor_id/<int:sensor_id>', methods = ['GET'])
def get_sensor_by_sensor_id(sensor_id):
        return SensorController.get_sensor_by_sensor_id(sensor_id)

@iot_bp.route('/api/sensor/add_sensorData', methods = ['POST'])
def add_sensorData():
        return SensorController.add_sensorData()



""" @iot_bp.route('/api/user/<int:user_id>', methods = ['GET'])
def add_sensorData()
css

"""

@iot_bp.route('/api/sensor/get_sensor_data_by_id', methods = ['POST'])
def get_sensorData_by_time_interval():
        return SensorController.get_sensorData_by_id()