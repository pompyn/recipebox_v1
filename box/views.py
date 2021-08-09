from django.shortcuts import render
from box.models import Recipe, Author

# Create your views here.


def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


