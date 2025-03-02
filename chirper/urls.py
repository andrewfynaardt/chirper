"""
chirper/urls.py
Created: 2025-02-16
Updated: 2025-03-02

Included the app-specific URLs for the chirper app.
Better maintainability, organization, and scalability then just having all URLs in cong/urls.py
"""

from django.urls import path
from .views import chirp_view
from django.views.generic import TemplateView

urlpatterns = [
    # The template for chirp_form
    path('chirp_form/', chirp_view, name='chirp_form'),
    # The success page after user uploaded their chirp
    path('success/', TemplateView.as_view(template_name="chirper/success.html"), name='success'),
]
