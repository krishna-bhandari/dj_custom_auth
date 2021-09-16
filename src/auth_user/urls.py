from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginApiView.as_view()),
    # path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('email-verify/', views.VerifyEmail.as_view(), name='verify_email'),
]