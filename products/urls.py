from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('product/<int:pk>', DetailedPage.as_view(), name='detail'),
    path('cart/', CartDetail.as_view(), name='cart_detail'),
    path('<int:pk>/', addToCart, name='add_to_cart'),
    path('product/<int:pk>/delete>', DeleteProduct.as_view(), name='delete'),
    path('product/<int:pk>/update', UpdateProduct.as_view(), name='update'),
    path('product/create', CreateProduct.as_view(), name='create')
]