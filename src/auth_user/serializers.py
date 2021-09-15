from .models import DevSetup
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()
class LoginSerializers(TokenObtainPairSerializer):
    password = serializers.CharField(max_length = 68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=66,required=False)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['user_type'] = user.user_type
        return token

    def validate(self, attrs):
        field_name = DevSetup.objects.first().login_field
        password = attrs.get('password', '')
        username = attrs.get('username')

        if field_name == "e": 
            if User.objects.filter(email = username).exists():
                username = User.objects.get(email = username).username
                user = auth.authenticate(username = username, password = password)
            else:
                raise AuthenticationFailed('Email not Valid')

        elif field_name == "u":
            if User.objects.filter(username = username).exists():
                username = User.objects.get(username = username).username
                user = auth.authenticate(username = username, password = password)
            else:
                raise AuthenticationFailed('Username not registered')
        else:
            if User.objects.filter(email = username).exists():
                username = User.objects.get(email = username).username
            user = auth.authenticate(username = username, password = password)
        if not user:
            raise AuthenticationFailed('Invalid Crendential, Try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled contact admin')

        tokens = self.get_token(user)
        refresh_token = str(tokens)

        access_token = str(tokens.access_token)

        return {
            'access': access_token,
            'refresh': refresh_token,
        }

