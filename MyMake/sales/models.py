from django.db import models
from customers.models import Customer

from resources.base import BaseModel
# Create your models here.
class Sales(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    price = models.IntegerField()
    category = models.CharField(max_length=150)
    

    def __str__(self):
        return f"{self.id}"

    def __repr__(self):
        return f"{self.customer}"
