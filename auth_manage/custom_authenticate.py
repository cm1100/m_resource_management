from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from resources.models import User
import jwt


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        """
        Override this method to authenticate a User instance based on JWT token.
        """
        auth = super().authenticate(request)
        if auth is not None:
            return auth

        # Custom authentication for User model
        token = self.get_validated_token(self.get_raw_token(request))
        try:
            user = User.objects.get(id=token['user_id'])
        except User.DoesNotExist:
            raise AuthenticationFailed("No such user found")
        return (user, token)
