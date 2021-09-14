from .models import CustomUserPermission
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
# Register your models here.

admin.site.register(CustomUserPermission)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email']
    list_display_links = ['username']
    class  Meta:
        model = User