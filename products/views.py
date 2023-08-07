from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from . models import Product, Cart
# Create your views here.


class HomePage(generic.ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'


class DetailedPage(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


def cartDetail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    cart_total_items = sum([item.quantity for item in cart_items])

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "cart_total_items": cart_total_items,
    }
    return render(request, "products/cart.html", context)


def addToCart(request,pk):
    try:
        cart_item = Cart.objects.get(user=request.user, product_id=pk)
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
    except:
        Cart.objects.create(user=request.user, product_id=pk)

    return redirect("home")


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