from flask import request
from services.iot_services import IotService
from views.iot_views import IotView

class AlertsController:
       
       
        @staticmethod
        def create_alert():
                data = request.get_json()
                alert_id = data.get("alert_id")
                alert_time = data.get("alert_time")
                messege = data.get("messege")
                alert_type = data.get("alert_type")
                alert_status = data.get("alert_status")
                alert = IotService.create_alert(alert_id, alert_time, messege, alert_type, alert_status)
                return IotView.render_alerts(alert), 200

        @staticmethod
        def get_all_alerts():
                alerts = IotService.get_all_alerts()
                return IotView.render_alerts(alerts), 200
           
        @staticmethod
        def turn_off_alert_by_alert_id(alert_id):
                alert = IotService.turn_off_alert_by_alert_id(alert_id)
                if  alert:
                        return IotView.render_success("alert status turned offf"), 200
    

        @staticmethod
        def get_alerts_by_time_interval():
                data = request.get_json()
                starttime = data.get("starttime")
                endtime = data.get("endtime")
                alerts = IotService.get_alert_by_time_interval(starttime, endtime)
                if not alerts:
                        return IotView.render_error("the time stamp is not correct"), 404
                return IotView.render_alerts(alerts), 200
