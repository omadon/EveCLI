from server import EveRestServer

REST_SCHEMA = {
    'login': '/accounts/actions/login/',
    'logout': '/accounts/actions/logout/',
    'intercepts': '/intercepts/intercepts/'
}

class EveServer(EveRestServer):
    def __init__(self, address, port, version):
        EveRestServer.__init__(self, address, port, version)

    def login(self, user, password):
        api_call = REST_SCHEMA['login']
        payload = {
            "username": user,
            "password": password
        }
        response = self.post_object(api_call, data=payload)
        self.set_cookies(response.cookies)
        return response

    def logout (self):
        api_call = REST_SCHEMA['logout']

        response = self.post_object(api_call, data=None)
        return response
