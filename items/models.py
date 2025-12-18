from django.db import models

class Item(models.Model):
    item_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')],
        default='ACTIVE'
    )

    def __str__(self):
        return self.name
