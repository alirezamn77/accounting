from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IncomeSerializer
from .models import Income
# Create your views here.

class IncomeViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Income.objects.all()
     
    # specify serializer to be used
    serializer_class = IncomeSerializer

    filter_fields = (
        'personiD',
        
    )