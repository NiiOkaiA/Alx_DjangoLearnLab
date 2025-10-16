from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=50)

class Supplier(models.Model):
    supplier_id=models.IntegerField(primary_key=True)
    supplier_name=models.CharField(max_length=50)

class WarehouseManager(models.Model):
    Manager_id=models.IntegerField(primary_key=True)
    Manager_name=models.CharField(max_length=60)

class Warehouse(models.Model):
    warehouse_id=models.IntegerField(primary_key=True)
    warehouse_name=models.CharField(max_length=50)
    warehouse_manager=models.ForeignKey(WarehouseManager,on_delete=models.CASCADE,related_name='manager')

class Product(models.Model):
    Product_id=models.AutoField(primary_key=True)
    Product_name=models.CharField(max_length=50)
    Cost_price=models.IntegerField()
    product_description=models.TextField(null=True)
    Selling_price=models.IntegerField()
    Date_added=models.DateTimeField(default=timezone.now)
    Last_updated=models.DateTimeField(auto_now=True)
    Quantity=models.IntegerField()
    Category_Id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    Supplier_Id=models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='supplier')
    Warehouse_Id=models.ForeignKey(Warehouse,on_delete=models.CASCADE,related_name='warehouse')


