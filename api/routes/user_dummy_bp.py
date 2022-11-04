from flask import Blueprint

from api.controllers import user_dummy_controller

user_dummy_bp = Blueprint('user_dummy', __name__, url_prefix="/dummy/users")

user_dummy_bp.route('/', methods=['GET'])(user_dummy_controller.create)
