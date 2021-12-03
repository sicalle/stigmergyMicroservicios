from django.urls import path
from . import views

urlpatterns =  [
        path('list/', views.get_ordenes, name='ordenesList'),
        path('get/', views.get_orden, name='get_orden'),
        path('update/', views.update_orden, name='update_orden'),
        path('getPrio/', views.get_ordenes_priorizadas, name='getPrio_orden'),
        path('create/', views.create_orden, name='create_orden')

]
