from django.shortcuts import render
from .models import Product,WarehouseManager,Supplier,Category,Product
from rest_framework import generics
from .serializers import WarehouseManagerSerializer,SupplierSerializer,CategorySerializer,ProductSerializer
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework import viewsets
# Create your views here.


class add_products(generics.CreateAPIView):
    model=Product
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    permission_classes=[IsAuthenticated,IsOwner]

class list_product(generics.ListAPIView):
    model=Product
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class update_product(generics.UpdateAPIView):
    model=Product
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class delete_product(generics.DestroyAPIView):
    model=Product
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    permission_classes=[IsAuthenticated]

#    def get_queryset(self):
 #       return Product.objects.create()
'''
class ProductViewSet(viewsets.ModelViewSet)
    queryset=Product.Objects.all()
    serializer_class=ProductSerializer

    def get_queryse(self):
        return Product.objects.create()
'''
    
