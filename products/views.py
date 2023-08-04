from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from . models import Product, Cart
# Create your views here.

# def homePage(request):
#     return render(request, 'products/home.html')


class HomePage(generic.ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'


class DetailedPage(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class CartDetail(generic.ListView):
    model = Cart
    template_name = 'products/cart.html'
    context_object_name = 'orders'
    cart_total = Cart.get_cart_item()
    context = {'cart_total': cart_total}




def addToCart(request, pk):
    product = Product.objects.get(id=pk)
    try:
        order = Cart.objects.get(product=product)
        order.quantity += 1
        order.save()
    except:
        order = Cart.objects.create(product=product)
        order.save()

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    return redirect('home')


class UpdateProduct(generic.edit.UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products/update.html'
    success_url = reverse_lazy('home')


class CreateProduct(generic.CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/create.html'
    success_url = reverse_lazy('home')


class DeleteProduct(generic.edit.DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('home')