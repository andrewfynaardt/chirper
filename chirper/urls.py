"""
chirper/urls.py
Created: 2025-02-16
Updated: 2025-03-02

Included the app-specific URLs for the chirper app.
Better maintainability, organization, and scalability then just having all URLs in cong/urls.py
"""

from django.urls import path
from .views import (
    chirp_view,
    home,
    profile,
    like_chirp,
    still_dev,
    replies_page,
    reply_to_chirp,
    like_reply,
)
from django.shortcuts import render


urlpatterns = [
    path("", home, name="home"),  # Template for home page
    path("profile/", profile, name="profile"),  #  Profile page
    # The success page after user uploaded their chirp
    path(
        "success/",
        lambda request: render(request, "success.html"),
        name="success",
    ),  # Success page
    path("chirper/reply/like/<int:reply_id>/", like_reply, name="like_reply"),
    path("null/", still_dev, name="still_dev"),
    path("like/<int:chirp_id>/", like_chirp, name="like_chirp"),
    path("create/", chirp_view, name="chirp_view"),
    path("chirper/<int:chirp_id>/replies/", replies_page, name="replies_page"),
    path("chirper/reply/<int:chirp_id>/", reply_to_chirp, name="reply_to_chirp"),
]
