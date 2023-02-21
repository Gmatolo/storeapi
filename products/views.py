from django.db.models import Q
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .forms import *
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
# products =[
#     {'id':1, 'name':'Courses'},
#     {'id':2, 'name':'Movies'},
#     {'id':3, 'name':'Subscriptions'},
#     {'id':4, 'name':'Tickets'},
# ]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_list(request):
    # context = {'products' : products}
    q = request.GET.get('q') if request.GET.get('q') !=None else ""
    
    # products = Product.objects.filter(name__istartswith='s')
    products = Product.objects.filter(
        Q(name__icontains=q)  | 
        Q(description__icontains=q)

    )
    return render(request, "products/product_list.html", {"products": products} )

def get_a_product(request):
    try: 
        product = Product.objects.get(pk=1)
        return render(request, "products/create_product.html", {"product": product})
    except Product.DoesNotExist:
        return ""
    
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect("home")
    
    return render(request, "products/create_product.html", {"form": form})


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    print("update test 1")

    if request=='POST':
        form = ProductForm(request.POST, instance=product)
        print("update test 2")
        if form.is_valid():
            print(f"this is the updatd form {form}")
            form.save()
            print(f"this is the saved form {form}")
            return redirect('home')
    context = {"form": form}
    return render(request, "products/create_product.html", context )

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.POST:
        product.delete()
        return redirect('home')
    return render(request, "products/delete_product.html", {'product':product})






