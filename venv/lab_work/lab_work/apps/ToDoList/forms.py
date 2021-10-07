from django import forms
from .models import Task

class ContactForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"