from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from rest_framework.exceptions import ValidationError
from .models import DevSetup
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken


class Util:
    @staticmethod
    def send_mail(data):
      
        smtpsetting = DevSetup.objects.first()
        backend = EmailBackend(port = smtpsetting.email_port, username = smtpsetting.email_host_user, password = smtpsetting.email_host_password, fail_silently=False)
        email = EmailMessage(subject= data['email_subject'], body=data['email_body'], from_email= smtpsetting.email_host_user,to=[data['email_receiver']], connection=backend)
        email.send()



def send_register_verification(data):
    user = User.objects.get(email = data['email'])
    token = RefreshToken.for_user(user).access_token
    current_site = DevSetup.objects.first().frontend_url
    relative_link = reverse('verify_email')
    absurl = current_site + relative_link+"token="+str(token)
    email_body = 'Hi '+user.username+', Use this link to verify your email: \n'+ absurl
    data = {
        'email_subject': 'Email Confirmation',
        'email_body': email_body,
        'email_receiver': user.email
    }
    try:
        Util.send_mail(data)
    except:
        raise ValidationError({"error":"please setup host email in dev setup"})
