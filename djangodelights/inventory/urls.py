from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('ingredients/', views.IngredientList.as_view(), name = 'ingredients'),
    path('ingredients/<pk>/delete', views.IngredientDelete.as_view(), name = 'ingredient_delete'),
    path('menu_items/', views.MenuItemList.as_view(), name = 'menu_items'),
    path('purchases/', views.PurchasesList.as_view(), name = 'purchases'),
]