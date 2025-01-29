from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length= 180)
    descriptions = models.TextField()
    price =  models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField()
    
    def __str__(self):
        return self.name