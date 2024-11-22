from flask import request
from services.iot_services import IotService
from views.iot_views import IotView


class DeviceController:
        @staticmethod
        def get_all_devices():
                devices = IotService.get_all_devices()
                return IotView.render_device(devices)

        @staticmethod
        def get_device_by_device_id(device_id):
                devices = IotService.get_device_by_device_id(device_id)
                if not devices:
                        return IotView.render_error("this user has not installed any iot device"), 404
                return IotView.render_devices(devices), 200
        
        @staticmethod
        def get_information_of_devices(house_id):
                devices = IotService.get_information_of_devices(house_id)
                if not devices:
                        return IotView.render_error("no iot device is installed in this house", house_id), 404
                return IotView.render_devices(devices), 200
        
        @staticmethod
        def add_device():
                data = request.get_json()
                device_id = data.get("device_id")
                house_id = data.get("house_id")
                devicename = data.get("devicename")
                devicetype = data.get("devicetype")
                devicestatus = data.get("devicestatus")
                device = IotService.add_device(device_id, house_id, devicename, devicetype, devicestatus)
                if device:
                        return IotView.render_devices(device)
                return IotView.render_error("device not added"), 404

        @staticmethod
        def toggle_device(device_id):
                device = IotService.togle_device(device_id)
                if device:
                        return IotView.render_success("the status of device is changed"), 200
                