from django.db import models
from customers.models import Customer

# Create your models here.
from resources.base import BaseModel

class Products(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    description = models.CharField(max_length=150, default='Sem descrição')
    quantity = models.IntegerField()
    category = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
