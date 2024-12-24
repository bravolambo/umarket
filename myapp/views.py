# your_app/views.py

from django.shortcuts import render,redirect
from .models import Product  # Assuming you have a Product model
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
def chat_page(request):
    return render(request, 'chat.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('verification')  # Redirect to home page after saving
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
def index(request):
    products = Product.objects.all()
    total_products = products.count()  # Count the total products
    return render(request, 'index.html', {'products': products, 'total_products': total_products})

# View for the about page (if needed)
def about(request):
    return render(request, 'about.html')

# View for the contact page (if needed)
def contact(request):
    return render(request, 'contact.html')

# View for the services page (if needed)
def services(request):
    return render(request, 'services.html')
