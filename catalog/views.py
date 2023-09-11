from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, "catalog/index.html", context)


def base(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, "catalog/base.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, телефон: {phone}, сообщение: {message}.')

    return render(request, 'catalog/contacts.html')


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/catalog.html', context)


def products(request, pk):
    context = {
        'object_list': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/products.html', context)
