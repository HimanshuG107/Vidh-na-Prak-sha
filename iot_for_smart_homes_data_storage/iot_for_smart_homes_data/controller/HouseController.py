from flask import request
from services.iot_services import IotService
from views.iot_views import IotView

class HouseController:

    @staticmethod
    def get_all_houses():
        houses = IotService.get_all_houses()
        return IotView.render_houses(houses), 200
           
    @staticmethod
    def get_house_by_house_id(house_id):
        house = IotService.get_house_by_house_id(house_id)
        if not house:
            return IotView.render_error("this house id does not exisst in the dattabase"), 404
        return IotView.render_houses(house)

    @staticmethod
    def add_house():
        data = request.get_json()
        house_id = data.get("house_id")
        user_id = data.get("user_id")
        location_id = data.get("location_id")
        room_id = data.get("room_id")
        house_no = data.get("house_no")
        new_house = IotService.add_house(house_id, user_id, location_id, room_id, house_no)
        if new_house:
            return IotView.render_success("house added successfully"), 200
        return IotView.render_houses(new_house)


