from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('get', views.getRoutes1, name="routes1"),
    path('products', views.getProducts, name="products"),
    path('products/<str:pk>/', views.getProduct, name="product"),
    
]
