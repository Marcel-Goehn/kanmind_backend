from rest_framework import generics
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]