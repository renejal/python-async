import json
from domain.authentication import Token
from repositories.error_response import get_error_from_response
from conf.settings import SessionManager
from conf import settings


class LoginRepository:
    host = settings.NAVITAIRE_HOST

    def get_token(self) -> Token:
        session = SessionManager().get()
        login_request = {
            "credentials": {
                "username": settings.NAVITAIRE_USERNAME,
                "password": settings.NAVITAIRE_PASSWORD,
                "domain": settings.NAVITAIRE_DOMAIN,
                "channelType": settings.NAVITAIRE_CHANNEL_TYPE
            }
        }
        login_response = session.post(
            f"{self.host}/api/nsk/v1/token",
            headers={
                "content-type": "application/json"
            },
            verify=False,
            data=json.dumps(login_request))
        if login_response.status_code == 201:
            json_obj = login_response.json()
            token = Token.from_dict(json_obj['data'])
            return token
        print(login_response.text)
        raise get_error_from_response(login_request)
