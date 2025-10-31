from rest_framework import generics
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
    
    
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        filtered_user = User.objects.get(email=request.data['email'])
        request.data['username'] = filtered_user.username
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'fullname': user.username,
            'email': user.email,
            'user_id': user.pk
        })