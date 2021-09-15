from .serializers import LoginSerializers
from rest_framework_simplejwt.views import TokenRefreshView


class LoginApiView(TokenRefreshView):
    serializer_class = LoginSerializers