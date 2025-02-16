from django.db import models

# Create your models here.


class Users(models.Model):
    """
    Information related to each user is stored here.
    
    Attributes:
        user_name (str): The name of the user.
        email (str): The email address of the user.
    """

    user_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.user_name

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
    Users,
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
    
