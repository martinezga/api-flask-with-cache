from flask import request, make_response
from werkzeug.exceptions import NotFound

from api.configurations.database import cache
from api.configurations.settings import ApiConfig
from api.helpers.common import clean_query_params
from api.models.user_model import UserModel
from api.serializers.user_serializers import (
    UserSerializer,
    UserListSerializer,
)

FILTER_FIELDS_ALLOWED = [
    'name',
    'lastname',
    'email',
]


@cache.cached(query_string=True)
def list_all():
    message = {
        'detail': {},
        'status_code': 400,
    }
    query_params_received = request.args
    query_params = clean_query_params(query_params_received)

    # optionals query param for pagination
    page = int(query_params.get('page', 1))
    per_page = int(query_params.get('per_page', ApiConfig.ROWS_PER_PAGE))
    # optionals query param for filtration
    filter_fields = {}
    for filter_key in FILTER_FIELDS_ALLOWED:
        filter_value = query_params.get(filter_key)
        if filter_value:
            filter_fields[filter_key] = filter_value
    # Improvement: Implement searching and ordering
    try:
        query_pag = UserModel.filtered_users(filter_fields).paginate(
            page=page,
            per_page=per_page,
            max_per_page=100
        )
        # Improvement: Implement users role to allow admins see the audit fields
        serializer = UserListSerializer(query_pag.items)

        message['data'] = serializer.data
        message['status_code'] = 200
        message['detail']['has_more'] = query_pag.has_next
        message['detail']['next_page'] = query_pag.next_num
        message['detail']['count'] = len(query_pag.items)
    except NotFound:
        message['detail']['error'] = 'Not Found'
        message['status_code'] = 404

    response = make_response(message, message['status_code'])
    response.headers['X-custom-header'] = 'custom header'

    return response


def create():
    message = {
        'detail': '',
        'status_code': 400,
    }
    # Verify data was sent
    if not request.data:
        message['detail'] = 'No data sent'

    # When detail is empty means there are not previous errors
    if not message['detail']:
        body = request.json
        data = {
            'name': body.get('name'),
            'lastname': body.get('lastname'),
            'email': body.get('email'),
        }
        serializer = UserSerializer(data=data)
        serializer.create()
        if serializer.has_errors:
            message['detail'] = serializer.errors
        else:
            message['detail'] = 'Created'
            message['status_code'] = 200

    response = make_response(message, message.get('status_code'))

    return response
