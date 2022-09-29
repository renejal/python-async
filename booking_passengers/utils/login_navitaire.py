from utils.exceptions import LoginTimeoutError


class SetNavitaireHost:
    def __init__(self, request, host):
        self.host = host
        self.request = request
        self.__api_token = request.session.get("Token")
        self.__username =  request.session.get("Username")

    def get_api_token(self):
        return self.__api_token

    def set_api_token(self, token):
        if token != "":
            self.__api_token = token

    def get_logged_username(self):
        return self.__username

    def get_headers(self):
        token = self.get_api_token()
        if token is not None:
            return {
                "Content-type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        else:
            raise LoginTimeoutError()
