from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True, default="")
    supplier_price = models.IntegerField(default=0)
    selling_price= models.IntegerField(default=0)
    quantity= models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_modified', '-date_created']

    def __str__(self) -> str:
        return self.name
    
class Categories(models.Manager):
    name = models.CharField(max_length=100)
    
