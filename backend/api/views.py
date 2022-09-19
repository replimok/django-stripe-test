from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Item, Order

import stripe

stripe.api_key = settings.STRIPE_API_KEY


def create_session(items, discount=None, tax_rates=None, currency=None):
    session_tax_rates = []
    if tax_rates:
        for tax_rate in tax_rates:
            session_tax_rates.append(tax_rate.tax_rate_id)
    session_items = []
    for item in items:
        session_items.append({
            "price": item.price_id,
            "quantity": 1,
            'tax_rates': session_tax_rates
        })
    session_discounts = []
    if discount:
        session_discounts.append({
            'coupon': f'{discount.coupon_id}',
        })
    if currency is None:
        currency = 'usd'
    response = stripe.checkout.Session.create(success_url="https://example.com/success",
                                              cancel_url="https://example.com/cancel",
                                              line_items=session_items,
                                              mode="payment",
                                              discounts=session_discounts,
                                              currency=currency
                                              )
    return response


def buy_order_view(request, order_id):
    query = Order.objects.all()
    order = get_object_or_404(query, id=order_id)
    response = create_session(items=order.items.all(),
                              discount=order.discount,
                              tax_rates=order.tax_rates.all())
    return JsonResponse(data=response)


def buy_item_view(request, item_id):
    query = Item.objects.all()
    item = get_object_or_404(query, id=item_id)
    response = create_session([item])
    return JsonResponse(data=response)


def buy_item_view_eur(request, item_id):
    query = Item.objects.all()
    item = get_object_or_404(query, id=item_id)
    response = create_session([item], currency='eur')
    return JsonResponse(data=response)


def buy_item_view_jpy(request, item_id):
    query = Item.objects.all()
    item = get_object_or_404(query, id=item_id)
    response = create_session([item], currency='jpy')
    return JsonResponse(data=response)


def item_view(request, item_id):
    query = Item.objects.all()
    item = get_object_or_404(query, id=item_id)
    context = {
        'item': item,
    }
    return render(request, 'item.html', context=context)


def order_view(request, order_id):
    query = Order.objects.all()
    order = get_object_or_404(query, id=order_id)
    context = {
        'items': order.items.all(),
        'order': order
    }
    return render(request, 'order.html', context=context)
