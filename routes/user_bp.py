from flask import Blueprint

from controllers import user_controller

user_bp = Blueprint('user_bp', __name__, url_prefix="/auth/users")

user_bp.route('', methods=['GET'])(user_controller.list_all)
user_bp.route('', methods=['POST'])(user_controller.create)
