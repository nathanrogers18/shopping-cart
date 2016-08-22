from django.contrib import admin

# Register your models here.
from .models import Cart, CartProduct, Product


admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Product)
