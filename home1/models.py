from django.db import models

# Create your models here.
class candy(models.Model):
    name = models.CharField(max_length=200)
    quantity =  models.IntegerField()
    img = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.name