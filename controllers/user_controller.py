from flask import jsonify, request


def list_all():
    response = {
       "detail": "Looks like there are no registered users!"
    }
    return jsonify(response)
