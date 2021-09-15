from .models import CustomUserPermission, DevSetup, UserType
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
# Register your models here.

admin.site.register(CustomUserPermission)
admin.site.register(DevSetup)
admin.site.register(UserType)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email']
    list_display_links = ['username']
    class  Meta:
        model = User