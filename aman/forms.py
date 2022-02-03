from django import forms
from .models import FixRequest

class FixForm(forms.ModelForm):
    class Meta:
        model = FixRequest
        fields = ['short_desc','store','admen_aman']
