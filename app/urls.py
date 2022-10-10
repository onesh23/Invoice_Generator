from django.urls import path
from app . views import *

urlpatterns = [
    path('',index,name='index'),
    path('buy_product/<int:pk>',buy_product,name='buy_product'),
    path('bill_pdf',bill_pdf,name='bill_pdf')
]
