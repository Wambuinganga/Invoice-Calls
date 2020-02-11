from django.urls import path, include
from rest_framework import routers
from .views import InvoiceViewSet, MonthViewSet

router=routers.DefaultRouter()
router.register('Invoice',InvoiceViewSet)
router.register('Month',MonthViewSet )

urlpatterns=[
path("",include(router.urls)),
]

