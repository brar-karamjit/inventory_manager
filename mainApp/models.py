from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity =  models.IntegerField()
    img = models.CharField(max_length=2000)
    barcode = models.CharField(max_length=100, unique=True, null=True, blank=True, default='default_barcode_value')  # Unique barcode for each product


    def __str__(self) -> str:
        return self.name
    

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    #https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
    username = models.CharField(max_length=100)  # Store username as a string
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.username} changed {self.product.name} from {self.old_quantity} to {self.new_quantity} on {self.timestamp}"