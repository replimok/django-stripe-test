from django.urls import re_path
from .views import buy_item_view, item_view, buy_order_view, order_view, \
    buy_item_view_eur, buy_item_view_jpy

urlpatterns = [
    re_path(r'^buy/(?P<item_id>\d+)$', buy_item_view),
    re_path(r'^buy-eur/(?P<item_id>\d+)$', buy_item_view_eur),
    re_path(r'^buy-jpy/(?P<item_id>\d+)$', buy_item_view_jpy),
    re_path(r'^item/(?P<item_id>\d+)$', item_view),

    re_path(r'^buy/order/(?P<order_id>\d+)$', buy_order_view),
    re_path(r'^order/(?P<order_id>\d+)$', order_view),
]