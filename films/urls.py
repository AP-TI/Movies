from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='films'), path('search/', views.search, name='search')]