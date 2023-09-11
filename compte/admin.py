from django.contrib import admin
from .models import CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_commissariat')
    list_filter = ('is_commissariat',)

admin.site.register(CustomUser, CustomUserAdmin)
