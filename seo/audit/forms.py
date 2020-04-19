from django import forms


class GenerateForm(forms.Form):
    domain_name = forms.CharField()
