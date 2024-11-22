from flask import request
from services.iot_services import IotService
from views.iot_views import IotView

class GivesController:
    @staticmethod
    def create_gives_tuple():
        data = request.get_json()
        device_id = data.get("device_id")
        alert_id = data.get("alert_id")
        new_gives_tuple = IotService.create_gives_tuple(device_id, alert_id)
        if new_gives_tuple:
                return IotView.render_success("a new tuple is created"), 200
        return IotView.render_error("tupple is not created"), 404

