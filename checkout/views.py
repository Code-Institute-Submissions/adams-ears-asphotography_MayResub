from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I6Em0B7GlGKlm1dQ2SnKeDhvkeDALutnJPZMUfwcd4TSoFjW1vUlGj0IQB9yjP7D2DdwrEmbuWhNcer1TKs08ED00AMcVQAnZ',
    }

    return render(request, template, context)
