from flask import request
from services.iot_services import IotService
from views.iot_views import IotView

class OwnesController:
        @staticmethod
        def create_ownes_tuple():
                data = request.get_json()
                user_id = data.get("user_id")
                device_id = data.get("device_id")
                new_ownes_tuple = IotService.create_ownes_tuple(user_id, device_id)

                if new_ownes_tuple:
                        return IotView.render_success("a new tuple is added"), 200
                return IotView.render_error("tuple is not added"), 404
