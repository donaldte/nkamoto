from django.contrib import admin
from .models import Commissariat, MotoVolee


class CommissariatAdmin(admin.ModelAdmin):
    list_display = ('nom_commissariat', 'adresse_commissariat', 'responsable_commissariat', 'telephone_commissariat',
                    'email_commissariat', 'ville_commissariat')
    search_fields = (
        'nom_commissariat', 'adresse_commissariat', 'responsable_commissariat__username', 'ville_commissariat')
    list_filter = ('ville_commissariat',)
    # Additional customization options go here


class MotoVoleeAdmin(admin.ModelAdmin):
    list_display = ('moto', 'commissariat', 'commentaire', 'date_vol')
    search_fields = ('moto__name', 'commissariat__nom_commissariat', 'commentaire')
    list_filter = ('date_vol',)
    # actions = ['mark_as_found']
    #
    # def mark_as_found(self, request, queryset):
    #     # Custom action logic here
    #     queryset.update(found=True)
    #
    # mark_as_found.short_description = "Marquer comme etant trouvee"  # Description for the admin action


# Register your models with the custom admin classes
admin.site.register(Commissariat, CommissariatAdmin)
admin.site.register(MotoVolee, MotoVoleeAdmin)
