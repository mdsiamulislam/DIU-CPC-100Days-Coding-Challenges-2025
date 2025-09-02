from django.http import JsonResponse
from django.shortcuts import render
from .serializers import CarCompanySerializer
from .models import CarCompany
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListCarCompanies(APIView):
    def get(self, request, format=None):
        companies = CarCompany.objects.all()
        serializer = CarCompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CarCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
