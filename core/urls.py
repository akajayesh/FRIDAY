from django.urls import path
from jinja2 import Template
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('bye/', TemplateView.as_view(template_name='bye.html')),
    path('clear/', views.clear_history, name='clear')
]