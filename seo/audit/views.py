from django.views.generic import TemplateView, FormView
from audit import forms
from services.senuto import test_script
from audit.models import AuditGeneration
# Create your views here.


class GenerateView(FormView):
    template_name = 'audit/generate.html'
    form_class = forms.GenerateForm
    success_url = 'success/'

    def form_valid(self, form):
        task_result = test_script.call_api_sync(form.cleaned_data)
        print(task_result)
        file_path = task_result['file_path']
        AuditGeneration.objects.create(file_path=file_path)
        return super().form_valid(form)


class GenerateSuccessView(TemplateView):
    template_name = 'audit/generate_success.html'
