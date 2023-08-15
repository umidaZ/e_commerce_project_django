from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/delete', RetriveProduct.as_view()),
    path('<int:id>/update', RetriveProduct.as_view()),
    path('<int:id>/', RetriveProduct.as_view()),
    path('', ShowProducts.as_view()),
]