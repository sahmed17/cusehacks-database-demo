from django.db import models
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey('Customer', related_name="orders", on_delete=models.CASCADE, blank=True, null=True)
    c_name = models.CharField(max_length=200)
    ship_date = models.DateField()
