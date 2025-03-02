from django.db import models

# To use the user ID from the Django default user table
from django.contrib.auth.models import User

# Create your models here.


class Chirps(models.Model):
    """
    Information related to each chirp are stored here.
    
    Attributes:
        chirp_body (str): Content of the chirp.
        user_id (int): (foreign key) The user that created this chirp.
        created_time (datetime): The date and time when the chirp was created.
        parent_chirp_id (int): (foreign key) The Chirp ID of the parent Chirp (if this Chirp is a reply).
    """
    chirp_body = models.CharField(max_length=255)
    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
        ) 
    created_time = models.DateTimeField()
    parent_chirp_id = models.ForeignKey(
        'self', # Another chirp's ID
        on_delete=models.SET_NULL,
        null=True
        ) 

    def __str__(self):
        return self.chirp_body[:20]
    
