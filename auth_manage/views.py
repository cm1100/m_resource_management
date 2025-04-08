from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from resources.models import User
from django.contrib.auth import authenticate
from .token import UserToken
import jwt

class ObtainUserTokenPairView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password,user.password):  # You can replace this with hashed password check
            refresh = UserToken.for_user(user)
            access = refresh.access_token
            return Response({
                'refresh': str(refresh),
                'access': str(access),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)




class RefreshUserTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        try:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            return Response({'access': str(access_token)})
        except jwt.ExpiredSignatureError:
            return Response({"detail": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.JWTError:
            return Response({"detail": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
