from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='restaurant_logo/', blank=False)

    #Funciona para cuando se muestre en el Administrador de Django se muestre el nombre y no "Restaurant object"
    def __str__(self):
        return self.name
