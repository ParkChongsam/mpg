from django.urls import path
from . import views

# app_name = 'firstPage'
urlpatterns = [
    path('', views.index, name='Homepage'),
    path('predictMPG', views.predictMPG, name='predictMPG'),
    path('viewDataBase', views.viewDataBase, name='viewDataBase'),
    path('updateDataBase', views.updateDataBase, name='updateDataBase')
]
