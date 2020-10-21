from django import forms
from ap1.models import ap1Person


class ap1PersonForm(forms.ModelForm):
    class Meta:
        model = ap1Person
        fields = '__all__'
