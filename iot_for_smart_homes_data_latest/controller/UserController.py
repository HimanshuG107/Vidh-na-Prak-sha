from flask import request
from services.iot_services import IotService
from views.iot_views import IotView


class UserController:
    @staticmethod
    def get_all_users():
        users =IotService.get_all_users()
        return IotView.render_users(users)

    @staticmethod
    def get_user_by_username(name):
        user = IotService.get_user_by_username(name)
        if user:
            return IotView.render_success("the user has been found"), 200
        return IotView.render_user(user)

    @staticmethod
    def get_user(user_id):
        user = IotService.get_user(user_id)
        if not user:
            return IotView.render_error("the user can not be found"), 404
        return IotView.render_user(user), 200
   
    @staticmethod
    def create_user():
        data = request.get_json()
        # user_id = data.get("userid")
        name = data.get("name")
        email = data.get("email")
        password_hash = data.get("password_hash")
        user = IotService.create_user( name, email, password_hash )

        if user:
            return IotView.render_success("the user is created successfully"), 200

    @staticmethod
    def user_login():
        data = request.get_json()

        email = data.get("email")
        password_hash = data.get("password_hash")

        user =IotService.verify_user(email, password_hash)

        if user:
            return IotView.render_success("the user logged in successfully"), 200
        return IotView.render_error("log in failed due to wrong username or password"), 401
