from django.db import models

# Create your models here.
from resources.base import BaseModel

class Customer(BaseModel):    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    total_spend = models.IntegerField()
