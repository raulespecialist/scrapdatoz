# -*- coding: utf-8 -*-
from datoz.models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('sku', 'nombre', 'descripcion', 'price', 'imagen')