import requests

class EveRestServer (object):
    def __init__(self, address, port, version):
        self.cookies = None
        address = address + ":" + port
        self.base_url = "/".join(['https:/', address, 'api', version])

    def _send_request(self, method, path, data=None):
        response = None
        url = self.base_url + path
        try:
            response = requests.request(method, url, json=data, cookies=self.cookies, verify=False)
        except requests.exceptions.RequestException as e:
            print '%sr %s %s'%('ERROR: Error calling', url, e.message)
        return response


    def post_object(self, api_call, data=None):
        return self._send_request('POST',api_call, data)

    def get_object(self, api_call, data=None):
        return self._send_request('GET', api_call, data)

    def put_object(self, api_call, data=None):
        return self._send_request('PUT', api_call, data)

    def set_cookies(self, new_cookie):
        self.cookies = new_cookie
