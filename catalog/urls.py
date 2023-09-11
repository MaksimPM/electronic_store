from django.urls import path
from catalog.views import index, base, contacts, catalog, products

urlpatterns = [
    path('', index),
    path('base/', base),
    path('contacts/', contacts),
    path('catalog/', catalog),
    path('products/<int:pk>', products, name='products'),
]
