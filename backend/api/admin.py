from django.contrib import admin
from .models import Item, Order, Discount, TaxRate

admin.site.register(Item, admin.ModelAdmin)
admin.site.register(Discount, admin.ModelAdmin)
admin.site.register(TaxRate, admin.ModelAdmin)
admin.site.register(Order, admin.ModelAdmin)
