from django.db import models
from car.models import CarModel

# Create your models here.

class FuelType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_liter = models.DecimalField(max_digits=10, decimal_places=2)
    usage_in_cars = models.ManyToManyField(CarModel, related_name='fuel_types')

    def __str__(self):
        return self.name
