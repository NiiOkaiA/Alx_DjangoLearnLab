from django.shortcuts import render
from .models import Product,WareHouseManager,Supplier,Category,Product
from rest_framework import generics
from .serializers import WarehouseManagerSerializer,SupplierSerializer,CategorySerializer,ProductSerializer
from django.views.generic.edit import CreateView,UpdateView,DeleteView


from rest_framework import viewsets
# Create your views here.


class add_product(generics.CreateAPIView):
    model=Product
    serializer_class=ProductSerializer

#    def get_queryset(self):
 #       return Product.objects.create()




'''
class ProductViewSet(viewsets.ModelViewSet)
    queryset=Product.Objects.all()
    serializer_class=ProductSerializer

    def get_queryse(self):
        return Product.objects.create()
'''
    
