from flask import request
from services.iot_services import IotService
from views.iot_views import IotView

class SensorController:
    @staticmethod
    def get_all_sensors():
        sensors = IotService.get_all_sensors()
        return IotView.render_sensors(sensors)

    @staticmethod
    def toggle_sensor(sensor_id):
        sensor = IotService.toggle_sensor(sensor_id)
        if sensor:
            return IotView.render_success("the status of the sensor is toggled"), 200    

    @staticmethod
    def add_sensor():
        data = request.get_json()
        sensor_id = data.get("sensor_id")
        device_id = data.get("device_id")
        sensor_type = data.get("sensortype")
        sensor_status = data.get("sensorstatus")
        sensor = IotService.add_sensor(sensor_id, device_id, sensor_type, sensor_status)
        if sensor:
            return IotView.render_sensors(sensor), 200

    @staticmethod
    def get_sensor_by_sensor_id(sensor_id):
        sensor = IotService.get_sensor_by_sensor_id(sensor_id)
        if not sensor:
            return IotView.render_error("sensor  not  found"), 404
        return IotView.render_sensors(sensor), 200


    @staticmethod
    def add_sensorData():
        data = request.get_json()
        sensorData_id = data.get("sensorData_id")
        sensor_id = data.get("sensor_id")
        data_value = data.get("data_value")

        new_sensorData = IotService.add_sensorData(sensorData_id, sensor_id, data_value)
        if new_sensorData:
            return IotView.render_success("new sensor data is added  successfully"), 200
        return IotView.render_error("sensor data can not be added"), 404
