"""
chirper/models.py
Updated: 2025-03-02

Include custom models for the chirper app.
Uses the Django default User model for other models.
"""


from django.db import models

# Create your models here.

# To use the user ID from the Django default user table
from django.contrib.auth.models import User

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
    

class Reply(models.Model):
    """
    Represents a reply to a chirp.
    
    Attributes:
        user (User): The user who made the reply.
        chirp (Chirps): The chirp being replied to.
        content (str): The reply content.
        created_at (datetime): The timestamp of when the reply was made.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirps, related_name="replies", on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.user_name} to Chirp {self.chirp.id}"


class UserFollowing(models.Model):
    """
    Represents a user following another user.
    
    Attributes:
        user (User): The user who is following.
        following_user (User): The user being followed.
        created_at (datetime): The timestamp when the follow occurred.
    """
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'following_user')  # Prevent duplicate follows

    def __str__(self):
        return f"{self.user.user_name} follows {self.following_user.user_name}"


