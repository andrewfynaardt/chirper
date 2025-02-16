"""
admin.py
Updated: 2025-02-16

Include the models and database I want to view through superuser.
"""

from django.contrib import admin
from .models import Chirps, Users

# Register your models here.

admin.site.register(Chirps)
admin.site.register(Users)