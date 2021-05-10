from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views import generic
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()

    #search code
    search_items = request.GET.get('search_items')
    if search_items !='' and search_items is not None:
        products = Product.objects.filter(name__icontains = search_items)


    #paginator
    paginator = Paginator(products,4)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render (request,'products/index.html',{'products':products})


class ProductDetail(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    def get_queryset(self):
        return Product.objects.all()
    
