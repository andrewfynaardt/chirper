from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Chirps(models.Model):
    """
    Information related to each chirp is stored here.
    
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
        null=True,
        related_name="chirps"
    ) 
    created_time = models.DateTimeField(default=timezone.now)
    parent_chirp_id = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True
    ) 
    likes = models.ManyToManyField(User, related_name="liked_chirps", blank=True)

    # Function that returns the total number of likes
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.chirp_body[:20]
    

class Reply(models.Model):
    """
    Represents a reply to a chirp.
    
    Attributes:
        user (User): The user who made the reply.
        chirp (Chirps): The chirp being replied to.
        content (str): The reply content.
        created_time (datetime): The timestamp of when the reply was made.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirps, related_name="replies", on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} to Chirp {self.chirp.id}"


class UserFollowing(models.Model):
    """
    Represents a user following another user.
    
    Attributes:
        user (User): The user who is following.
        following_user (User): The user being followed.
        created_time (datetime): The timestamp when the follow occurred.
    """
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'following_user')  # Prevent duplicate follows

    def __str__(self):
        return f"{self.user.username} follows {self.following_user.username}"
