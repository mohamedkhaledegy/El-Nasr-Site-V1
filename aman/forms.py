from dataclasses import field
from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from .models import FixRequest , Visit


class FixForm(forms.ModelForm):
    class Meta:
        model = FixRequest
        fields = ['short_desc','store','admen_aman']

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['done']
        widgets = {
            'date_visit': widgets.DateInput(attrs={'type': 'date'}),
            'content': widgets.SelectMultiple()
        }

