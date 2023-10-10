from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
class HomeView(TemplateView):
  template_name = "inventory/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["ingredients"] = Ingredient.objects.all()
    context["menu_items"] = MenuItem.objects.all()
    context["recipe_requirements"] = RecipeRequirement.objects.all()
    context["purchases"] = Purchases.objects.all()
    return context

class IngredientList(ListView):
  model = Ingredient
  template_name = "vetoffice/ingredient_list.html"

class MenuItemList(ListView):
  model = MenuItem
  template_name = "vetoffice/menu_item_list.html"

class PurchasesList(ListView):
  model = Purchases
  template_name = "vetoffice/purchases_list.html"

class IngredientDelete(DeleteView):
  model = Ingredient
  template_name = "vetoffice/ingredient_delete.html"
  success_url = "/ingredients"