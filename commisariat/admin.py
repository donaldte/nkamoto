from django.contrib import admin

from .models import Commissariat, MotoVolee

# Register your models here.

class CommissariatAdmin(admin.ModelAdmin):
    list_display = ('nom_commissariat', 'adresse_commissariat', 'responsable')
    list_filter = ('responsable',)

class MotoVoleeAdmin(admin.ModelAdmin):
    list_display = ('moto', 'commissariat')
    list_filter = ('commissariat',)


admin.site.register(Commissariat, CommissariatAdmin)
admin.site.register(MotoVolee, MotoVoleeAdmin)