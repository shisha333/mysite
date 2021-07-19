from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


# Create your models here.
class CustomOrder(models.Model):
    title = models.CharField(_("Title "), max_length=50)
    name = models.CharField(_("Name "), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phone"), max_length=70)
    address = models.CharField(_("Address"), max_length=70)
    
    
    class Meta:
        db_table = 'customer_orders'
        managed = True
        verbose_name = 'customer order'
        verbose_name_plural = 'customer orders'

class Payment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    objects = models.Manager()

    def __str__(self):
        return self.title

class Cal(models.Model):

    length = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    
    @property
    def area(self):
       return self.length * self.width


# Create your models here.
