from django.contrib import admin

from moto.models import DeclarationVol, ImageMoto, Moto


class ImageMotoInline(admin.TabularInline):
    model = ImageMoto

class MotoAdmin(admin.ModelAdmin):
    inlines = [ImageMotoInline]
    list_display = ('numero_matricule', 'type_moto', 'proprietaire')
    search_fields = ('numero_matricule', 'proprietaire__username', 'type_moto', 'description')

class DeclarationVolAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'moto', 'date_vol', 'quartier')
    list_filter = ('date_vol',)
    search_fields = ('utilisateur__username', 'moto__numero_matricule', 'quartier')

admin.site.register(DeclarationVol, DeclarationVolAdmin)
admin.site.register(Moto, MotoAdmin)
