from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=1)

    def get_total(self):
        price = Product.objects.get(id=self.product.id)
        return price.price * self.quantity


    def __str__(self):
        return f'{self.product.name} :  {self.quantity}'


    def get_cart_total(self):
        total = 0
        cart_items = Cart.objects.all()
        for cart_item in cart_items:
            total += cart_item.get_total()
        return total

    @classmethod
    def get_cart_item(cls):
        quantity = 0
        cart_items = cls.objects.all()
        for cart_item in cart_items:
            quantity += cart_item.quantity
        return quantity