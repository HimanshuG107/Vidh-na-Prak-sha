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
        sensor_type = data.get("sensor_type")
        sensor_status = data.get("sensor_status")
        sensor = IotService.add_sensor(sensor_id, device_id, sensor_type, sensor_status )
        if sensor:
            return IotView.render_sensor(sensor), 200

    @staticmethod
    def get_sensor_by_sensor_id(sensor_id):
        sensor = IotService.get_sensor_by_sensor_id(sensor_id)
        if not sensor:
            return IotView.render_error("sensor  not  found"), 404
        return IotView.render_sensor(sensor), 200


    @staticmethod
    def add_sensorData():
        data = request.get_json()
        sensor_data_id = data.get("sensor_data_id")
        sensor_id = data.get("sensor_id")
        data_value = data.get("data_value")
        sensor_time = data.get("sensor_time")
        unit =  data.get("unit")

        new_sensorData = IotService.add_sensorData(sensor_data_id, sensor_id, data_value , sensor_time,  unit )
        if new_sensorData:
            return IotView.render_success("new sensor data is added  successfully"), 200
        return IotView.render_error("sensor data can not be added"), 404
    
    @staticmethod
    def get_sensorData_by_time_interval():
        data = request.get_json()
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        sensordata = IotService.get_sensor_data_by_time_interval(start_time, end_time)
        return IotView.render_sensorData(sensordata)