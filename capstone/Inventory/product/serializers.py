from rest_framework import serializers
from .models import Product


#serialized models
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['Product_id','Product_name','Cost_price','Selling_price','Quantity','Category_Id','Supplier_id','Warehouse_id','Date_added','Last_updated']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_id','warehouse_name','warehouse_manager']


class WarehouseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=WarehouseManager
        fields=['Manager_id','Manager_name']
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields=['supplier_id','supplier_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category_id','category_name']
