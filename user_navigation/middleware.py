from user_navigation.library import authenticate_user
import time


class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before")
        isValidUser, username = authenticate_user(request)
        if isValidUser:
            if 'last_request' in request.session:
                elapsed = time.time() - request.session['last_request']
                request.session['username'] = username
                if elapsed > 60:
                    del request.session['last_request']
                    request.session.flush()
            request.session['last_request'] = time.time()
        else:
            if 'last_request' in request.session:
                del request.session['last_request']
        response = self.get_response(request)
        return response


