# serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from resources.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(source='email')  # Replace with custom field if needed

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        data = super().validate(attrs)
        data['tenant_id']= self.user.tenant_id
        return data
