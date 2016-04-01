from server import EveRestServer
from eveapi import EveServer

API_ADDRESS = '192.168.110.60'
API_PORT = '2305'
API_VER = '1'
USER = 'api'
PASSWD = 'eveapipassword'

def evecli():
    server = EveServer(API_ADDRESS, API_PORT, API_VER)
    result = server.login(USER, PASSWD)
    print "Authenticating... Server returned: " + str (result.status_code) + "\n"

    result = server.logout()
    print "Logging out... Server returneed: " + str (result.status_code) + "\n"

    print "All done"

if __name__ == '__main__':
    evecli()