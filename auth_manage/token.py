from rest_framework_simplejwt.tokens import RefreshToken
from resources.models import User
from django.contrib.auth import authenticate

class UserToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        """
        Generate a new token for a specific user instance.
        """
        if not isinstance(user, User):
            raise ValueError('User must be an instance of User model')
        data = super().for_user(user)

        data['tenant_id']=user.tenant_id

        return data

    def get_user(self):
        """
        Retrieve the user associated with this token.
        """
        user_id = self.get('user_id')
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Exception("User does not exist")
