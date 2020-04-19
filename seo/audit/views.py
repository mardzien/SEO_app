from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class GenerateView(TemplateView):
    template_name = 'audit/generate.html'
