from django.db import models
from fuel_type.models import FuelType

# Create your models here.

class CarCompany(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CEO(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    company = models.OneToOneField(CarCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CarModel(models.Model):
    name = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    fuel_type = models.ManyToManyField(FuelType, related_name='car_models')

    def __str__(self):
        return self.name
    

class CarDetails(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car_model.name} - {self.year}"
        