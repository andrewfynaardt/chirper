"""
forms.py
Created: 2025-2-16
Updated: 2025-2-16

Contains the form to accept user chirp input. 
"""

from django import forms
from .models import Chirps


class ChirpForm(forms.ModelForm):
    """
    Create the form based on the existing Chirps class.
    Only allow the user to inout chirp_body.
    """
    class Meta:
        model = Chirps
        fields = ['chirp_body']