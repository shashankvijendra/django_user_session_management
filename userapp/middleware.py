from django.contrib.sessions.models import Session
# from userapp.models import  *


class onesessionuser:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            a=request.user.Loginuser_user
            current_session_key = a.session_key
            if current_session_key and current_session_key != request.session.session_key:
                Session.objects.get(Session_key = current_session_key).delete()
            
            request.user.Loginuser_user.session_key = request.session.session_key
            request.user.Loginuser_user.save()
        print("Request start!")
        response = self.get_response(request)
        print("Request middkeware!",response)
        # print(response)

        # Code to be executed for each request/response after
        # the view is called.

        return response