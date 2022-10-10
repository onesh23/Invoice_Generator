from django.contrib import admin
from app . models import Seller,Buyer,Product

# Register your models here.

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','phone','date']

admin.site.register(Buyer)
admin.site.register(Product)
