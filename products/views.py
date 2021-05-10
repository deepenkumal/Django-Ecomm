from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views import generic

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render (request,'products/index.html',{'products':products})


class ProductDetail(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    def get_queryset(self):
        return Product.objects.all()
    
