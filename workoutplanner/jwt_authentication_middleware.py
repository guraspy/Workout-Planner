from django.http import HttpResponse
import jwt
from django.conf import settings
from rest_framework import status

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.auth_exempt_views = [
            'RegisterView',
            'LoginView',
            'SpectacularAPIView',
            'SpectacularSwaggerView', 
            'SpectacularRedocView'
        ]

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.cls.__name__ in self.auth_exempt_views:
            # Skip JWT authentication for views specified in auth_exempt_views
            return None
        
        token = request.COOKIES.get('jwt')
        if not token:
            return HttpResponse("Unauthorized!", status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user_id = payload['id']
        except jwt.InvalidSignatureError:
            return HttpResponse('Invalid JWT! Unauthorized!', status=status.HTTP_401_UNAUTHORIZED)
        except jwt.ExpiredSignatureError:
            return HttpResponse('Expired JWT! Unauthorized!', status=status.HTTP_401_UNAUTHORIZED)
        
        return None