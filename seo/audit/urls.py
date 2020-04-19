from django.urls import path
from audit import views

app_name = 'audit'

urlpatterns = [
    path('generate/', views.GenerateView.as_view(), name='generate'),
    path('generate/success/', views.GenerateSuccessView.as_view(), name='generate_success'),
    # path('about/', views.AboutView.as_view(), name = 'about'),
]

