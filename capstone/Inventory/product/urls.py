from django.urls import path
from .views import add_products,list_product,update_product,delete_product


urlpatterns=[
    path('product/new/',add_products.as_view(),name='newproduct'),
    path('product/list/',list_product.as_view(),name='productlist'),
    path('product/update/',update_product.as_view(),name='productupdate'),
    path('product/delete/',delete_product.as_view(),name='productdelete'),


    ]
