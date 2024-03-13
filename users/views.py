from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from workoutplanner import settings
from .serializers import UserAuthSerializer, UserSerializer
from .models import User
import jwt, datetime
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets


class RegisterView(APIView):
    @extend_schema(request=UserAuthSerializer, responses={200: UserAuthSerializer})
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    @extend_schema(request=UserAuthSerializer, responses={200: UserAuthSerializer})
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        
        response = Response()
        
        # Returning token via cookies
        # httponly=True means that the cookie is accessible only via HTTP headers and not accessible via JavaScript.
        # This is a security measure to prevent cross-site scripting (XSS) attacks.
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message':'success'
        }
        
        return response
    
    
class LogoutView(APIView):
    @extend_schema(responses={200: UserAuthSerializer})
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
   
    
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # GET
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    # PUT
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Resource updated successfully'}, status=status.HTTP_204_NO_CONTENT)