from django.shortcuts import render
from .forms import InvoiceForm
from .models import InvoiceForm
import csv,io 
from django.contrib import messages

def invoice_upload(request):
	template=invoice_upload.html
	csv_data=Invoice.objects.all()

	if request.method=="GET":
		return render(request, template)
		csv_file=request.FILES["csv_file"]
		
	if not csv_file.name.endswith('.csv'):
		messages.error(request,'File is not CSV type')
	
	file_data = csv_file.read().decode("utf-8")	

io_string = io.StringIO(data_set)
next(io_string)
for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    _, created = Invoice.objects.update_or_create(
        contact_name=column[0],
        invoice_number=column[1],
        invoice_date=column[2],
        due_date=column[3],
        description=column[4],
        quantity=column[5],
        unit_amount=column[6]
    )
context = {}
return render(request, template, context)	







# Create your views here.
