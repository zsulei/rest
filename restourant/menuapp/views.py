from django.shortcuts import render
from .models import Dishes, Ingredients, KitchenTypes
from django.db.models import Q
from thefuzz import fuzz
from Levenshtein import distance
# Create your views here.


def MenuView(request):
    context = {
        'dishes': Dishes.objects.all(),
        'ingredients': Ingredients.objects.all(),
        'types': KitchenTypes.objects.all()
    }
    return render(request, 'dishes.html', context=context)


def dishesByIngredient(request, ingredientId):
    queryset = Dishes.objects.filter(Q(ingredient1=ingredientId) |
                                     Q(ingredient2=ingredientId) |
                                     Q(ingredient3=ingredientId))
    return render(request, 'dishbyingredient.html', {'dishesByIngredient': queryset})


def dishesByWeight(request):
    searchweight = float(request.GET.get('WeightSearch'))
    queryset = Dishes.objects.filter(weight__gte=searchweight)
    return render(request, 'dishbyweight.html', {'dishesByWeight': queryset})


def dishes_by_name(request):
    search_result = request.GET.get('NameSearch')
    for dish in Dishes.objects.all():
        if distance(search_result, dish.name) <= 2:
            queryset = dish.name
        else:
            queryset = Dishes.objects.filter(name__icontains=search_result)
    return render(request, 'dishbyname.html', {'dishes_by_name': queryset})


