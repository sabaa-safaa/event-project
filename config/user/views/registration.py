from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework import generics
from ..serializers import UserSerializer


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
