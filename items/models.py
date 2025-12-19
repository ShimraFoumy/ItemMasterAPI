from django.db import models

class Item(models.Model):
    item_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    status = models.CharField(max_length=10)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def is_below_reorder(self):
        return self.quantity <= self.reorder_level

    def __str__(self):
        return f"{self.item_code} - {self.name}"
