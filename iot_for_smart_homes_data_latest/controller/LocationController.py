from flask import request
from services.iot_services import IotService
from views.iot_views import IotView

class LocationController:

    @staticmethod
    def get_all_locations():
        locations =IotService.get_all_locations()
        return IotView.render_locations(locations), 200  
    

    @staticmethod
    def get_location_by_location_id(location_id):
        location = IotService.get_location_by_location_id(location_id)
        if location:
            return IotView.render_location(location), 200
        return IotView.render_error("location not found"), 404

    @staticmethod
    def add_location():
        data = request.get_json()
        location_id = data.get("location_id")
        state = data.get("state")
        city = data.get("city")
        zipcode = data.get("zipcode")
        new_location = IotService.add_location(location_id, city, state, zipcode)
        if new_location:
            return IotView.render_success("location is added successfully"), 200
        return IotView.render_error("location does not added"), 404

