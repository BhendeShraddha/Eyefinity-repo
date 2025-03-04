from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDoctor, IsAdmin

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProfileView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor | IsAdmin]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "role": request.user.role
        })

