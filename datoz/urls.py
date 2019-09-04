# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('sourceslinio', views.ScrapLinio, name='ScrapLinio'),
    path('productos', views.product_list, name='product_list'),
    path('', views.index, name='index'),
]