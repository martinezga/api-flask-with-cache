from flask import Blueprint

from controllers.user_controller import (
    list_all,
)

user_bp = Blueprint('user_bp', __name__, url_prefix="/auth/users")

user_bp.route('', methods=['GET'])(list_all)
