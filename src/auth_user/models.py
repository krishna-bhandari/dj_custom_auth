from django.core import exceptions
from django.db import models
from django.contrib.auth.models import AbstractUser,ContentType


class User(AbstractUser):
    user_type = models.CharField(max_length=200,null=True,blank=True)
    is_verified = models.BooleanField(default = False)



class UserType(models.Model):
    title = models.CharField(max_length=200,unique=True)


class CustomUserPermission(models.Model):
    user_type = models.OneToOneField(UserType,on_delete = models.CASCADE)
    content_type = models.ManyToManyField(ContentType)


class VerifcationChoice(models.TextChoices):
    EMAIL_LINK = "el","Email Link"
    EMAIL_OTP = "eo","Email OTP"
    MOBILE_OTP = "mo","Mobile OTP"    


class LoginFieldChoice(models.TextChoices):
    EMAIL = "e","Email"
    USERNAME = "u","Username"
    BOTH = "b","Both"


class DevSetup(models.Model):
    """
    this model is used to create some setting fields.
    """
    default_user_type = models.ForeignKey(UserType,on_delete=models.CASCADE,null=True,verbose_name='Default User Type',help_text="selected user type will be default for normally registered user")
    verification_type = models.CharField(max_length = 2,choices = VerifcationChoice.choices,default=VerifcationChoice.EMAIL_LINK, verbose_name="Email Verification Method")
    email_port = models.IntegerField(default=587)
    email_host_user = models.EmailField(blank=True, null=True)
    email_host_password = models.CharField(max_length=255,blank=True, null=True, help_text="Use the app password not your actual password for the security reason.")
    
    login_field = models.CharField(max_length = 1,choices = LoginFieldChoice.choices,default = LoginFieldChoice.EMAIL,verbose_name="Required field for login",help_text="Choose the field which you want to use for login")
    frontend_url = models.URLField(max_length = 255,default = "http://localhost:3000",help_text = "this url is used while sending emails")
    # required_register_fields = models.ManyToManyField(User,blank = True,verbose_name = "Required register fields",help_text = "select multiple fields that you want to make compulsory for user registeration")

    def delete(self):
        raise exceptions.PermissionDenied("delete action not allowed")

