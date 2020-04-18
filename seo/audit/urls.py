from django.urls import path
from audit import views

urlpatterns = [
    path('generate/', views.GenerateView.as_view(), name='generate_audit'),
    # path('about/', views.AboutView.as_view(), name = 'about'),
]

