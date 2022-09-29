from conf import settings
from conf.settings import SessionManager
from domain.authentication import Token


class LoginRepository:
    
    def login(self) -> Token:
        login_endpoint = f"/api/nsk/v1/token"
        session = SessionManager().get()
        login_request = {
            "credentials": {
                "username": settings.NAVITAIRE_USERNAME,
                "password": settings.NAVITAIRE_PASSWORD,
                "domain": settings.NAVITAIRE_DOMAIN,
                "channelType": settings.NAVITAIRE_CHANNEL_TYPE
            }
        }
        login_response = session.post(f"{settings.NAVITAIRE_HOST}{login_endpoint}",
                headers={
                    "content-type": "application/json"
                }, json=login_request)

        if login_response.status_code != 201:
            login_response.raise_for_status()
        else:
            token = login_response.json()
            token = Token.from_dict(token['data'])
            return token