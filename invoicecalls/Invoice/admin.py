from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
	list_display=("contact_name","invoice_number","invoice_date","due_date","description","quantity","unit_amount")
	list_filter=("invoice_date",)
	search_fields=("contact_name","invoice_date")


admin.site.register(Invoice, InvoiceAdmin)

# Register your models here.
