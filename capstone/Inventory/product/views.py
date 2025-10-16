from django.shortcuts import render
from .models import Product,WareHouseManager,Supplier,Category,Product
from rest_framework import generics
from .serializers import WarehouseManagerSerializer,SupplierSerializer,CategorySerializer,ProductSerializer
# Create your views here.


class add_product(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    
