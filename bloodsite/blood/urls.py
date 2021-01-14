from django.urls import path
from . import views

urlpatterns = [
    path('', views.blood_main, name='blood_main'),
    path('doners/', views.doner_list, name='doner_list'),
    path('doner/<int:pk>/edit/', views.doner_edit, name='doner_edit'),
    path('doner/<int:pk>/detail/', views.doner_detail, name='doner_detail'),
    path('doner/new/', views.doner_new, name='doner_new'),
]