from django.views.generic import TemplateView, FormView, DetailView
from django.urls import reverse_lazy
from django.conf import settings
from audit import forms
from services.senuto import test_script
from audit.models import AuditGeneration
# Create your views here.


class GenerateView(FormView):
    template_name = 'audit/generate.html'
    form_class = forms.GenerateForm

    def __init__(self, *args, **kwargs):
        self.obj = None
        super().__init__(*args, **kwargs)

    def form_valid(self, form):
        task_result = test_script.call_api_sync(form.cleaned_data)
        print(task_result)
        prefix = f"{settings.MEDIA_DIR}/"
        file_path = task_result['file_path'].replace(prefix, "")
        print(file_path)
        self.obj = AuditGeneration.objects.create(file_path=file_path)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('audit:detail', kwargs={'pk': self.obj.uid})


class AuditGenerationDetailView(DetailView):
    context_object_name = 'audit_generation'
    queryset = AuditGeneration.objects.all()
    template_name = 'audit/detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class GenerateSuccessView(TemplateView):
    template_name = 'audit/generate_success.html'
