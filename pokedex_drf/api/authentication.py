from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BaseAuthentication
from rest_framework.views import APIView

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        is_browser_request = request.META.get('HTTP_USER_AGENT', '').lower().find('mozilla') > -1  

        if is_browser_request:
            return SessionAuthentication().authenticate(request)
        else:
            return TokenAuthentication().authenticate(request)