from django.db import models

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

    def __str__(self):
        return self.name