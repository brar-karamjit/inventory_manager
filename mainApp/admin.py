from django.contrib import admin
from mainApp.models import Product, Transaction

admin.site.register(Product)

# Register the Transaction model
admin.site.register(Transaction)

