from django.urls import path

from . import views
app_name = 'moto'
urlpatterns = [
    path('create_moto/', views.create_moto_with_images, name='create_moto'),
    path('detail_moto/<int:pk>/', views.detail_about_moto, name='detail_moto'),
    path('list_moto/', views.list_moto, name='list_moto'),
    path('list_moto_volee/', views.list_moto_volee, name='list_moto_volee'),
]