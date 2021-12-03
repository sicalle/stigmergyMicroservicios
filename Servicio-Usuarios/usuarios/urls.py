from django.urls import path
from . import views

urlpatterns =  [
    path('list/', views.get_usuarios, name='usuarios_list'),
    path('get/', views.get_usuario, name='get_usuario'),
]