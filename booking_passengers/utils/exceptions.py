class BaseDataException(Exception):
    def __init__(self, message="", code="", status_code=400):
        super().__init__(message, code)
        self.message = message
        self.code = code
        self.status_code = status_code


class BadRequestError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 400


class UnauthorizedError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 401


class ForbiddenError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 403


class NotFoundError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 404


class NotAllowedError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 405


class LoginTimeoutError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 440


class ServerError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 500


class NotImplementedError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 501


class BadGatewayError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 502


class ConnectionError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 503


class ServiceUnavailableError(BaseDataException):
    def __init__(self, message="", code=""):
        super().__init__(message, code)
        self.status_code = 503
