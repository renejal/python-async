import json
from requests import Response
from rest_framework import exceptions


class UnAuthorized(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 401
        self.code = code or "unauthorized"


class Forbidden(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 403
        self.code = code or "forbidden"


class NotFound(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 404
        self.code = code or "not_found"


class UnsupportedMediaType(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 415
        self.code = code or "unsupported_media_type"


class LoginTimeout(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 440
        self.code = code or "login_timeout"


class InternalServerError(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 500
        self.code = code or "internal_server_error"


class BadGateway(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 502
        self.code = code or "bad_gateway"


class GatewayTimeout(exceptions.APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        self.status_code = 504
        self.code = code or "gateway_timeout"


def parse_response_data(text, content_type) -> dict:
    if "xml" in content_type:
        # TODO: Parse xml and return dict
        pass
    if "json" in content_type:
        # TODO: Parse json and return dict
        pass
    return text


def get_error_from_response(response):
    """ This method traverses a json object (dict or list) and calls 'callback'
        on every element of type 'dict'. If the callback returns a result
        different to None, then that result is returned."""
    def traverse_dict(obj, callback):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if type(value) in (list, dict):
                    result = traverse_dict(value, callback)
                    if result:
                        return result
                else:
                    result = callback(key, value)
                    if result:
                        return value
        elif isinstance(obj, list):
            for elem in obj:
                if type(elem) in (list, dict):
                    result = traverse_dict(elem, callback)
                    if result:
                        return result
        return None

    if not isinstance(response, Response):
        return {"message": str(response)}
    exception_classes = {
        # 4xx
        400: exceptions.ValidationError,
        401: UnAuthorized,
        403: Forbidden,
        404: NotFound,
        405: exceptions.MethodNotAllowed,
        406: exceptions.NotAcceptable,
        415: UnsupportedMediaType,
        440: LoginTimeout,
        # 5xx
        500: InternalServerError,
        502: BadGateway,
        504: GatewayTimeout,
    }
    exception_class = (
        exception_classes.get(response.status_code) or
        exceptions.APIException
    )
    error_code = ""
    # TODO: Quitar el try except y usar la funcion parse_response_data
    try:
        json_obj = response.json()
        # Error id
        error_id = traverse_dict(
            json_obj,
            lambda key, value: "id" in str(key).lower())
        # Error type
        error_type = traverse_dict(
            json_obj,
            lambda key, value: "type" in str(key).lower())
        # Error code
        error_code = traverse_dict(
            json_obj,
            lambda key, value: "code" in str(key).lower())
        error_code = error_code or traverse_dict(
            json_obj,
            lambda key, value: str(key).lower() == "reason")
        # Error message
        error_message = traverse_dict(
            json_obj,
            lambda key, value: "msg" in str(key).lower())
        # Navitaire verbose message: "rawMessage"
        error_message = error_message or traverse_dict(
            json_obj,
            lambda key, value: str(key) == "rawMessage")
        error_message = error_message or traverse_dict(
            json_obj,
            lambda key, value: "message" in str(key).lower())
        detail = {
            "id": error_id or "",
            "type": error_type or "",
            "message": error_message or response.text,
            "status_code": response.status_code,
            "code": error_code or ""
        }
    except json.JSONDecodeError:
        detail = {
            "message": response.text,
            "status_code": response.status_code
        }

    if response.status_code == 415:
        return exception_class()
    if response.status_code == 405:
        return exception_class(None, detail=detail, code=error_code or "")
    return exception_class(detail=detail, code=error_code or "")