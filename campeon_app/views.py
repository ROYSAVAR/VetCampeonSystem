from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def home(request):
    return render(request, 'campeon_app/index.html')

def products(request):
    query = request.GET.get('name')  # Obtener el parámetro de búsqueda por nombre de la URL
    category = request.GET.get('category')  # Obtener el parámetro de búsqueda por categoría de la URL
    
    if query:
        # Filtrar por nombre usando contains (insensible a mayúsculas/minúsculas)
        products = Product.objects.filter(name__icontains=query)
    elif category:
        # Filtrar por categoría
        products = Product.objects.filter(category=category)
    else:
        # Traer todos los productos si no hay búsqueda
        products = Product.objects.all()
    
    categories = Product.CATEGORY_CHOICES  # Obtener las opciones de categoría
    
    return render(request, 'campeon_app/productos.html', {'products': products, 'categories': categories})
