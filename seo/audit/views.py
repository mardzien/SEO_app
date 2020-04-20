from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from audit import forms
from services.senuto import test_script
# Create your views here.


class GenerateView(FormView):
    template_name = 'audit/generate.html'
    form_class = forms.GenerateForm
    success_url = 'success/'

    def form_valid(self, form):
        # print(form.cleaned_data)
        zmienna = test_script.call_api(form.cleaned_data)
        print(zmienna)
        return super().form_valid(form)


class GenerateSuccessView(TemplateView):
    template_name = 'audit/generate_success.html'
