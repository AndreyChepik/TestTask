from django import forms
from .models import ClassifierModel

class CodeForm(forms.Form):
    """Form that asks for code and name parameters and tests inputs on validness"""
    code = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)

    def save(self):
        new_tag = ClassifierModel.objects.create(code = self.cleaned_data['code'], name = self.cleaned_data['name'])
        return new_tag
