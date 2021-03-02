from user_navigation.library import authenticate_user
import time, datetime


class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        request.session['last_visit'] = time.time()
        return response


