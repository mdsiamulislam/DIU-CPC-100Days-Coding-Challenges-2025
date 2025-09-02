from rest_framework import serializers
from .models import *


class CarCompanySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source = 'name',max_length=100)
    class Meta:
        model = CarCompany
        fields = ['title']