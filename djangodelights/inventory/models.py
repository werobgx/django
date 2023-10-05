from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return str(self.quantity) + " " + self.unit + " of " + self.name + " in inventory."
    
    class Meta:
        ordering = ["name"]

class MenuItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)

class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)