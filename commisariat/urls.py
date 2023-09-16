from django.urls import path 

from . import views

app_name = 'commisariat'

urlpatterns = [
    path('detail_moto_volee/<int:pk>/', views.detail_moto_volee, name='detail_moto_volee'),
]