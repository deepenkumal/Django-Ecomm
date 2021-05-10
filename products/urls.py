from django.urls import path
from . import views


app_name='products'
urlpatterns = [
    path('',views.index , name='index'),
    path('product/<str:pk>/detail',views.ProductDetail.as_view(),name='product_detail'),
]