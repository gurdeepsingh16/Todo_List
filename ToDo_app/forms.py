from django import forms
from .models import Todo_model

class Todo_form(forms.ModelForm):
    class Meta:
        model = Todo_model
        fields = "__all__"
        