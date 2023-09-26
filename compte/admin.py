from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_commissariat')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_commissariat')
    search_fields = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'numero_telephone', 'adresse_residence', 'numero_carte_identite')
    list_filter = ('user',)
    search_fields = ('user__username', 'numero_telephone', 'adresse_residence', 'numero_carte_identite')
    readonly_fields = ('user',)  # Fields that should be read-only in the admin


admin.site.register(Profile, ProfileAdmin)

admin.site.site_header = 'NKAMOTO Administration'
admin.site.site_title = 'NKAMOTO Admin'
admin.site.index_title = 'Bienvenue dans NKAMOTO Admin'
