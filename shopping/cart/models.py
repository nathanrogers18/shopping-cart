from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Cart(models.Model):
    cart_product = models.OneToManyField(CartProduct)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.cart_product_set.all()


class CartProduct(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "{}: {}".format(self.product, str(self.quantity))


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(validators=[MinValueValidator(0)],
                                decimal_places=2, max_digits=10)
    stock = models.IntegerField()

    CATEGORY_CHOICES = (
        "Electronics",
        "Books",
        "Music",
    )
    category = CharField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return "{}: Price: {}, Stock: {}, ".(name, price, stock, category)

#
# class Order(models.Model):
#     timestamp = models.DateTimeField(default=timezone.now)
#     total_cost = models.DecimalField(validators=[MinValueValidator(0)],
#                                      decimal_places=2, max_digits=10)
