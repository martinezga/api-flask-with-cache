from flask import request, make_response

from models.user_model import UserModel
from serializers.user_serializers import (
    UserSerializer,
    UserListSerializer,
)


def list_all():
    users = UserModel.query.all()
    serializer = UserListSerializer(users)

    response = make_response(serializer.data, 200)
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
