from django.urls import path
from . import views

# app_name = 'firstPage'
urlpatterns =[
    path('', views.index, name = 'Homepage'),
    path('predictMPG', views.predictMPG, name = 'predictMPG'),
]