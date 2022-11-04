from flask import request, make_response

from api.helpers.data_population import populate_data
from api.configurations.database import db
from api.helpers.common import clean_query_params


def create():
    message = {
        'detail': {},
        'status_code': 400,
    }
    query_params_received = request.args
    query_params = clean_query_params(query_params_received)

    # Users quantity to create
    qty = int(query_params.get('qty', 0))

    # Verify qty was sent
    if not qty:
        message['detail'] = 'No quantity sent'

    # When detail is empty means there are not previous errors
    if not message['detail']:
        qty_created, total_users = populate_data(db, qty)
        message['detail']['created'] = qty_created
        message['detail']['total registered'] = total_users
        message['status_code'] = 200

    response = make_response(message, message.get('status_code'))

    return response
