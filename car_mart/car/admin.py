from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CarCompany)
admin.site.register(models.CEO)
admin.site.register(models.CarModel)