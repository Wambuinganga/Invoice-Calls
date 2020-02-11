from django.db import models
from django.db.models import Func, F, Sum
import datetime


class Invoice(models.Model):
    contact_name=models.CharField(max_length=50)
    invoice_number=models.IntegerField()
    invoice_date=models.DateTimeField()
    due_date=models.DateTimeField()
    description = models.CharField(max_length=100)
    quantity=models.IntegerField()
    unit_amount=models.IntegerField()
    # csv_file = models.FileField(upload_to='files/',null=True)

def __str__(self):
    return self.contact_name

class Month(Func):
    function='Extract'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()

def total():
    total_invoices= (Invoice.objects
        .annotate(month=Month('invoice_date'))
        .values('month')
        .annotate(total=Sum('unit_amount'*'quantity'))
        .order_by('month'))
    for result in total_invoices:
        print (result) 
    raise Exception('stop')









# Create your models here.
