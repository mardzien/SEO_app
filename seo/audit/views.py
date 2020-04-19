from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from audit import forms
# Create your views here.


class GenerateView(FormView):
    template_name = 'audit/generate.html'
    form_class = forms.GenerateForm
    success_url = 'success/'


class GenerateSuccessView(TemplateView):
    template_name = 'audit/generate_success.html'
