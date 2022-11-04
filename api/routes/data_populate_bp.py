from flask import Blueprint

from api.controllers import data_populate_controller

data_populate_bp = Blueprint('data_populate', __name__, url_prefix="/populatedata")

data_populate_bp.route('/', methods=['GET'])(data_populate_controller.create)
