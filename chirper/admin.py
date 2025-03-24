"""
admin.py
Updated: 2025-03-02

Include the models and database I want to view through superuser.
"""

from django.contrib import admin
from .models import Chirp

# Django's default User model is already registered in the admin interface
# by the auth app. Don't need to register it again here.

# Register your models here.

admin.site.register(Chirp)