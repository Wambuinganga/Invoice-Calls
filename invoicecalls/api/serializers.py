from Invoice.models import Invoice, Month
from rest_framework import serializers


class InvoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model=Invoice
		fields="__all__"

class MonthSerializer(serializers.ModelSerializer):
	class Meta:
		model=Month
		fields="__all__"