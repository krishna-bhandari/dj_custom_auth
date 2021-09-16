from rest_framework.exceptions import ValidationError
from .utils import Util, send_register_verification
from .serializers import EmailVerificationSerializers, LoginSerializers, RegisterUserSerializers
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import generics,status, views
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from decouple import UndefinedValueError, config
import jwt


class LoginApiView(TokenRefreshView):
    serializer_class = LoginSerializers


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializers

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        send_register_verification(user_data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializers
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description="Enter the token you get from us in email", type=openapi.TYPE_STRING )
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token =request.GET.get('token')
        try:
            payload = jwt.decode(token, config('SECRET_KEY'), algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            user.is_active = True
            user.is_verified = True
            user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifer:
            return Response({'error': 'Activation Expire'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifer:
            return Response({'error': 'Invalid Token'}, status = status.HTTP_400_BAD_REQUEST)
        except UndefinedValueError:
            return Response({'error':'secret key missing. Please contact to admin'},status = status.HTTP_501_NOT_IMPLEMENTED)
