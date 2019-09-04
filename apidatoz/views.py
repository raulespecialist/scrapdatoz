from django.shortcuts import render
from datoz.models import Producto
from rest_framework import viewsets
from apidatoz.serializer import ProductoSerializer
import os
import json
#from exceptions import ValueError
from time import sleep

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que contiene los productos.
    """
    queryset = Producto.objects.all().order_by('-price')
    serializer_class = ProductoSerializer