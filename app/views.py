from django.shortcuts import render

from app.models import Buyer, Product, Seller

# Create your views here.


def index(request):
    products = Product.objects.all()
    seller = Seller.objects.all()
    
    return render(request,'index.html',{'products':products,'seller':seller,'msg':"dfghjkl"})

def buy_product(request,pk):
    products = Product.objects.get(pk=pk)
    print(pk)

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])

        # print(name)

        buy = Buyer(name=name,address=address,phone=phone)
        buy.save()

        amount = float(products.prod_price)
        prod_name = products.prod_name
        prod_desc = products.prod_desc
        prod_ratings = products.prod_ratings
        price = amount
        prod_quantity = quantity
        prod_total_price = amount * quantity

        seller = Seller.objects.all()

        data = {'id':pk,
                'prod_name':prod_name,
                'name':name,
                'prod_price':price,
                'address':address,
                'phone':phone,
                'prod_desc':prod_desc,
                'prod_quantity':prod_quantity,
                'prod_ratings':prod_ratings,
                'total_price':prod_total_price}
        return render(request,'bill_pdf.html',{'data':data,'seller':seller})

    return render(request,'buy_product.html')


def bill_pdf(request):
    seller = Seller.objects.all()
    return render(request,'bill_pdf.html',{'seller':seller})

