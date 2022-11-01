from flask import request, make_response

from configurations.settings import ApiConfig
from models.user_model import UserModel
from serializers.user_serializers import (
    UserSerializer,
    UserListSerializer,
)


def list_all():
    message = {
        'detail': {},
        'status_code': 400,
    }
    # optionals query param
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', ApiConfig.ROWS_PER_PAGE, type=int)

    query_pag = UserModel.query.paginate(
        page=page,
        per_page=per_page,
        max_per_page=100
    )
    serializer = UserListSerializer(query_pag.items)

    message['data'] = serializer.data
    message['status_code'] = 200
    message['detail']['has_more'] = query_pag.has_next
    message['detail']['next_page'] = query_pag.next_num
    message['detail']['count'] = len(query_pag.items)

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
