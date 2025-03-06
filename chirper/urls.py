"""
chirper/urls.py
Created: 2025-02-16
Updated: 2025-03-03

Included the app-specific URLs for the chirper app.
Better maintainability, organization, and scalability then just having all URLs in cong/urls.py
"""

from django.urls import path
from .views import chirpForm_view, home, chirp_view
from django.views.generic import TemplateView

urlpatterns = [
    # The homepage for chirper (include menu and chirp view)
    path('home/', home, name='home'),
    # To load the chirp_view (to display chirps from database)
    path("chirps/", chirp_view, name="chirp_view"),  
    # To load the chirpForm_view (so user can enter data)
    path('create_chirp/', chirpForm_view, name='chirp_form'),
    
]
