from flask import request


def form_response(code, error_message, response_data):

    response_body = {
        "code": code,
        "error_message": error_message,
        "response_data": response_data,
    }

    return response_body


def posted():
    """ Gets POSTed data. """

    return request.get_json(force=True, silent=True) or {}


def single_object_to_dict(obj):
    obj_to_dict = obj.__dict__
    del obj_to_dict['_sa_instance_state']
    return obj_to_dict
