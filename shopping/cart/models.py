from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(validators=[MinValueValidator(0)],
                                decimal_places=2, max_digits=10)
    stock = models.IntegerField()

    CATEGORY_CHOICES = (
        ("elec", "Electronics"),
        ("book", "Books"),
        ("music", "Music"),
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)

    def __str__(self):
        return "{}: Price: {}, Stock: {}, ".format(self.name,
                                                   self.price,
                                                   self.stock,
                                                   self.category)


class Cart(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.cart_product_set.all()


class CartProduct(models.Model):
    product = models.ForeignKey(Product)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "{}: {}".format(self.product, str(self.quantity))


#
# class Order(models.Model):
#     timestamp = models.DateTimeField(default=timezone.now)
#     total_cost = models.DecimalField(validators=[MinValueValidator(0)],
#                                      decimal_places=2, max_digits=10)
