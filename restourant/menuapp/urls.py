from django.urls import path
from .views import MenuView, dishesByIngredient, dishesByWeight
from .views import dishes_by_name


urlpatterns = [
    path('', MenuView, name='dishes'),
    path('dishbyingredient/<int:ingredientId>/', dishesByIngredient, name='dishbyingredient'),
    path('dishesbyweight/', dishesByWeight, name='dishbyweight'),
    path('dishesbyname/', dishes_by_name, name='dishbyname'),
]