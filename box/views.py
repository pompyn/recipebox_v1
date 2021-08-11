from django.shortcuts import render
from box.models import Recipe, Author

# Create your views here.


def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'recipes': recipes})

def add_author(request):
    pass

def add_recipe(request):
    pass
