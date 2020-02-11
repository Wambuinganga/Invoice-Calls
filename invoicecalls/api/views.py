from django.shortcuts import render
from Invoice.models import Invoice, Month
from .serializers import InvoiceSerializer, MonthSerializer    
from rest_framework import viewsets


class InvoiceViewSet(viewsets.ModelViewSet):
	queryset=Invoice.objects.all()
	serializer_class=InvoiceSerializer
	
class MonthViewSet(viewsets.ModelViewSet):
	queryset=Month()
	serializer_class=MonthSerializer


# Create your views here.
