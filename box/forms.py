from django import forms
from box.models import Author, Recipe


class AddAuthorForm(forms.Form):
    pass


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.TextInput)
