"""
chirper/urls.py
Created: 2025-02-16
Updated: 2025-03-02

Included the app-specific URLs for the chirper app.
Better maintainability, organization, and scalability then just having all URLs in cong/urls.py
"""

from django.urls import path
from .views import chirp_view, home, profile, like_chirp, still_dev
from django.shortcuts import render


urlpatterns = [
    # Template for home page
    path("", home, name="home"),
    # Profiles Template
    path("profile/", profile, name="profile"),
    # The success page after user uploaded their chirp
    path(
        "success/",
        lambda request: render(request, "success.html"),
        name="success",
    ),  # Success page
    path("null/", still_dev, name="still_dev"),
    path("like/<int:chirp_id>/", like_chirp, name="like_chirp"),
    path("create/", chirp_view, name="chirp_view"),
]
