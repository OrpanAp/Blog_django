from django import forms
from blogs.models import Category

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
