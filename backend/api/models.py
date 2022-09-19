from django.db import models
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_API_KEY


class TaxRate(models.Model):
    orders = models.ManyToManyField('Order', related_name='tax_rates')
    display_name = models.CharField(max_length=255, default='Sales Tax')
    inclusive = models.BooleanField(default=False)
    percentage = models.DecimalField(max_digits=4, decimal_places=2, default=7.25)
    country = models.CharField(max_length=255, default='US')
    state = models.CharField(max_length=255, default='CA')
    jurisdiction = models.CharField(max_length=255, default="US - CA")
    description = models.CharField(max_length=255, default='CA Sales Tax')

    @property
    def tax_rate_id(self):
        return stripe.TaxRate.create(
            display_name=self.display_name,
            inclusive=self.inclusive,
            percentage=self.percentage,
            country=self.country,
            state=self.state,
            jurisdiction=self.jurisdiction,
            description=self.description,
        )['id']


class Discount(models.Model):
    percent_off = models.IntegerField(default=20)
    duration = models.CharField(max_length=255, default="once")

    @property
    def coupon_id(self):
        # maybe only on first create idk
        return stripe.Coupon.create(percent_off=self.percent_off, duration=self.duration)['id']


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def price_id(self):

        return stripe.Price.create(
              unit_amount=int(self.price * 100),
              currency="usd",
              product=self.product_id,
              currency_options={
                'eur': {
                  'unit_amount': 9000
                },
                'jpy': {
                  'unit_amount': 12000
                }
              }
        )['id']

    @property
    def product_id(self):
        return stripe.Product.create(
            name=self.name,
            description=self.description,
        )['id']


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, related_name='orders', on_delete=models.SET_NULL, null=True, blank=True)
