from api.models import Item, Order, Discount, TaxRate
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.exists():
            print('Database is not empty...')
            return
        # admin
        User.objects.create_superuser('admin', password='adminpass')

        # Items
        Item.objects.create(name='Test 1', description='Some 1 description', price=10.10)
        Item.objects.create(name='Test 2', description='Some 2 description', price=20.20)

        # Discount
        discount = Discount.objects.create()

        # Order
        order = Order.objects.create(discount=discount)
        order.items.set(Item.objects.all())

        # TaxRate
        tax_rate = TaxRate.objects.create()
        tax_rate.orders.set([order])
        print('Completed...')
