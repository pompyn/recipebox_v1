from django import forms

class AddAuthorForm(forms.Form):
    pass


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    descripton = forms.CharField(max_length=100)
    time_required = forms.CharField(max_length=50)
    instructions = forms.Textarea()