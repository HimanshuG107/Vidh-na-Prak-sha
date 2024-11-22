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
            "room_no": house.room_no
        }
          
    @staticmethod
    def render_houses(houses):
        return [IotView.render_house(house) for house in houses]
    
    @staticmethod
    def render_location(location):
        return {
            "state": location.state,
            "city": location.city,
            "zip_code": location.zip_code
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