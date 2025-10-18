from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from models import Product,itemlog



class itemlog(models.Model):
    item =models.CharField(max_length=40)
    modification=models.CharField(max_length=30)
    time= models.DateTimeField(auto_now_add=True)


@receiver( post_save ,sender=Product):
def item_log_update(sender,instance,created,**kwargs):
    if instance.Quantity 
