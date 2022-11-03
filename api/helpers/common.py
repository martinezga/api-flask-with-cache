from werkzeug.datastructures import ImmutableMultiDict


def clean_query_params(received: ImmutableMultiDict):
    query_params = received.to_dict()

    for key, value in query_params.items():
        if value.endswith('/'):
            query_params[key] = value[:-1]

    return query_params
