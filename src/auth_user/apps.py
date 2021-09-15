from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_initial_data(sender, **kwargs):
    from .models import DevSetup
    if not DevSetup.objects.exists():
        DevSetup.objects.create()

class AuthUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_user'

    def ready(self):
        post_migrate.connect(create_initial_data,sender = self)
        

