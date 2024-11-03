from django.db import models

# Create your models here.


class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=208)
    item_des = models.CharField(max_length=208)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="data:image/png;base64,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")
