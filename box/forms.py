from django import forms
from box.models import Author
class AddAuthorForm(forms.Form):
    pass


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    descripton = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=50)
    instructions = forms.Textarea()