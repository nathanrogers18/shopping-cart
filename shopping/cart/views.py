from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Cart, CartProduct

# Create your views here.


class IndexView(generic.ListView):
    template_name = "cart/index.html"
    context_object_name = "cart_product_list"

    def get_queryset(self):
        self.cart = get_object_or_404(Cart, name=self.args[0])
        return Cart.objectes.filter(user=self.request.user)
