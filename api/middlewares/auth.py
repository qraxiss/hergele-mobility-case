from werkzeug.wrappers import Request, Response, ResponseStream
from config import config


class UserAuthMiddleware:
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        secret = request.headers.get("Authorization").replace("Bearer ", "")
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable

        if secret == config.BEARER:
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)