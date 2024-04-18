from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jumper/', views.jumper, name='jumper'),
    path('babe/', views.AddBabe, name='AddBabe'),
]