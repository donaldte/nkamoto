
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from moto import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('moto/', include('moto.urls')),
    path('compte/', include('compte.urls')),
]

# Servez les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)