"""
Project level conf/urls.py
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from chirper import views

urlpatterns = [
    # Admin and authentication URLs
    path("admin/", admin.site.urls),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/", include("allauth.urls")),
    path("", views.profile, name="profile"),
    path("chirper/", include("chirper.urls")),
    # Chirp-related URLs
    path("chirp/<int:chirp_id>/reply/", views.reply_to_chirp, name="reply_to_chirp"),
    # Follow/Unfollow URLs
    path("user/<int:user_id>/follow/", views.follow_user, name="follow_user"),
    path("user/<int:user_id>/unfollow/", views.unfollow_user, name="unfollow_user"),
    # User profile URL
    path("profile/<str:username>/", views.profile_view, name="profile"),
]
