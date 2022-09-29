import dataclasses
from rest_framework.response import Response


@dataclasses.dataclass
class HttpResponse:
    @staticmethod
    def Success(data):
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=200,
            data=data
        )

    @staticmethod
    def CustomError(status_code, message):
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=status_code,
            data={
                'message': message
            }
        )

    @staticmethod
    def Created(data):
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=201,
            data=data
        )

    @staticmethod
    def BadRequest(code, message):
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=400,
            data={
                'code': code,
                'message': message
            }
        )

    @staticmethod
    def Unauthorized():
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=401,
            data={
                'code': 'Unauthorized',
                'message': 'Acceso no autorizado'
            }
        )

    @staticmethod
    def Forbiden():
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=403,
            data={
                'code': 'Forbiden',
                'message': 'No cuenta con permisos'
            }
        )

    @staticmethod
    def ServerError(message):
        return Response(
            headers={
                "X-XSS-Protection": "1; mode=block"
            },
            status=500,
            data={
                'code': 'ServerError',
                'message': message
            }
        )
