from django.contrib import admin

from moto.models import DeclarationVol, ImageMoto, Moto


class ImageMotoInline(admin.TabularInline):
    model = ImageMoto


class DeclarationVolAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'moto', 'date_vol', 'quartier')
    list_filter = ('date_vol', 'quartier')
    search_fields = ('utilisateur__username', 'moto__numero_matricule', 'quartier', 'commentaire')


admin.site.register(DeclarationVol, DeclarationVolAdmin)


class MotoAdmin(admin.ModelAdmin):
    inlines = [ImageMotoInline]
    list_display = ('numero_matricule', 'type_moto', 'proprietaire', )
    list_filter = ('type_moto', 'proprietaire')
    search_fields = ('numero_matricule', 'type_moto', 'proprietaire__username', 'description')


admin.site.register(Moto, MotoAdmin)
