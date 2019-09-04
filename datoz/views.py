from django.shortcuts import render
import requests
import lxml.html
from datoz import models
from datoz.models import Producto
import datetime
from django.utils import timezone

# Recolector de datos de Linio.
def ScrapLinio(request):
    if request.method == 'GET':
        print ('Comenzando a cargar ultimos 10 articulos')
        html = requests.get('https://www.linio.com.mx/cm/solo-hoy-ofertas')
        doc = lxml.html.fromstring(html.content)

        li = 10
        nu = 0
        cont = 0

        while cont < li and nu < 100:
            print (nu)
            elementos = doc.xpath('.//div[@class="catalogue-product row"]')[nu]
            titles = elementos.xpath('.//span[@class="title-section"]/text()')[0]
            model = elementos.xpath('.//meta[@itemprop="model"]/@content')[0]
            prices = elementos.xpath('.//meta[@itemprop="price"]/@content')[0]
            image = elementos.xpath('.//meta[@itemprop="image"]/@content')[0]
            sku = elementos.xpath('.//meta[@itemprop="sku"]/@content')[0]
            print (nu)
            print (titles)
            print (prices)
            print (image)
            print (sku)
            nu = nu + 1
            if Producto.objects.filter(sku=sku).exists():
                print ('existe')
                continue
            product = models.Producto(usuario=request.user, sku=sku,
                                      nombre=titles, descripcion=model,
                                      price=prices, imagen=image)
            product.save()
            cont = cont + 1
        #return HttpResponse("OK")
        context= {
                'productos': cont,
            }
        return render(request, 'datoz/linio_succes.html', context)

def product_list(request):
    productos = Producto.objects.all()
    punk = "hola punk"
    print (Producto.objects.all())
    return render(request, 'datoz/product_list.html', {'productos': productos, 'punk': punk})

def index(request):
    return render(request, 'datoz/index.html', {})