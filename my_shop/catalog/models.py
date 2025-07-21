

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)           # Added name field (was missing)
    description = models.TextField()

    def __str__(self):
        return self.name

class InStock(models.Model):                          # Fixed typo: models.Model (not models.model)
    yes_or_no = models.BooleanField()

    def __str__(self):
        return "In stock" if self.yes_or_no else "Out of stock"

# class Items(models.Model):
#     item_name = models.CharField(max_length=60)
#     price = models.IntegerField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
#     in_stock = models.ForeignKey(InStock, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.item_name

class Items(models.Model):
    item_name = models.CharField(max_length=60)
    price     = models.IntegerField()
    category  = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,  # ok for FK
        blank=True
    )
    # ✅ BooleanField: no null, default False (or True)
    in_stock  = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name
        return self.name 