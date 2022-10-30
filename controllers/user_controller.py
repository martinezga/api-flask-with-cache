from flask import jsonify
from services.user_service import UserService


def list_all():
    response = UserService().get_all()

    return jsonify(response)
