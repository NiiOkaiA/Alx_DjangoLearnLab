from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from models import Product,itemlog





@receiver( post_save ,sender=Product):
def item_log_update(sender,instance,created,**kwargs):
    if instance.Quantity++:
        action='items restocked'

    elif instance.Quantity--:
        action='items sold'

    ChangeLog.objects.create(action=action,modification=Product.User)
