class IotView:
    @staticmethod
    def render_device(device):
        return {
            "house_id": device.house_id,
            "device_name": device.device_name,
            "device_type": device.device_type,
            "device_status": 'ON' if device.device_status else 'OFF'
        }
    
    @staticmethod
    def render_devices(devices):
        print(devices)
        return [IotView.render_device(device) for device in devices]
        
        
    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, user_id=None):
        response = {"message": message}
        if user_id:
            response["user_id"] = user_id
        return response
     
    @staticmethod
    def render_house(house):
        return {
            "user_id": house.user_id,
            "location_id": house.location_id,
            "house_no": house.house_no,
            "room_id": house.room_id
        }
          
    @staticmethod
    def render_houses(houses):
        return [IotView.render_house(house) for house in houses]
    
    @staticmethod
    def render_location(location):
        return {
            "state": location.state,
            "city": location.city,
            "zipcode": location.zipcode
        }
        
    @staticmethod
    def render_locations(locations):
        return [ IotView.render_location(location) for location in locations]
    
    
    @staticmethod
    def render_sensor(sensor):
        return {
            "device_id": sensor.device_id,
            "sensor_type": sensor.sensor_type,
            "sensor_status": 'ON' if sensor.sensor_status else 'OFF'
        }
    
    @staticmethod
    def render_sensors(sensors):
        return [IotView.render_sensor(sensor) for sensor in sensors]
     
    @staticmethod
    def render_user(user):
        return {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email
        }
    
    
    @staticmethod
    def render_users(users):
        return [ IotView.render_user(user) for user in users]
    
    @staticmethod
    def render_sensorData(sensorData_list):
        return [{
            "sensor_data_id": sensorData.sensor_data_id,
            "sensor_id": sensorData.sensor_id,
            "data_value": sensorData.data_value,
            "sensor_time": sensorData.sensor_time
        } for sensorData in sensorData_list]
        
    @staticmethod
    def render_alerts(alerts):
        return [{
            "alert_id": alert.alert_id,
            "alert_time": alert.alert_time,
            "message": alert.message,
            "alert_type": alert.alert_type,
            "alert_status": 'Alert' if alert.status else 'Resolved'
        } for alert in alerts]
    
    @staticmethod
    def render_alert(alert):
        return {
            "alert_id": alert.alert_id,
            "alert_time": alert.alert_time,
            "messege": alert.messege,
            "alert_type": alert.alert_type,
            "alert_status": 'Alert' if alert.alert_status else 'Resolved'
        }
        
    