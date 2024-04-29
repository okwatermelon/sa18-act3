from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
def show(request, id):
    user = get_object_or_404(Product, id=id)
    return render(request, 'show.html', {'product': user})    
# Create your views here.
