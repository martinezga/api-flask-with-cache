from flask import request, make_response

from api.helpers.user_dummy_creation import create_dummy_user
from api.configurations.database import db
from api.helpers.common import clean_query_params


def create():
    message = {
        'detail': {},
        'status_code': 400,
    }
    query_params_received = request.args
    query_params = clean_query_params(query_params_received)

    # Number of dummy users to create
    qty = int(query_params.get('qty', 1))

    # When detail is empty means there are not previous errors
    if not message['detail']:
        qty_created, total_users = create_dummy_user(db, qty)
        message['detail']['created'] = qty_created
        message['detail']['total registered'] = total_users
        message['status_code'] = 200

    response = make_response(message, message.get('status_code'))

    return response
