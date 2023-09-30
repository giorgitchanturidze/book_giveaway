from rest_framework import generics
from .serializers import CustomUserSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
