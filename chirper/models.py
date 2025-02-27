from django.db import models

# Create your models here.
class Reply(models.Model):
    """
    Represents a reply to a chirp.
    
    Attributes:
        user (Users): The user who made the reply.
        chirp (Chirps): The chirp being replied to.
        content (str): The reply content.
        created_at (datetime): The timestamp of when the reply was made.
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirps, related_name="replies", on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.user_name} to Chirp {self.chirp.id}"


class UserFollowing(models.Model):
    """
    Represents a user following another user.
    
    Attributes:
        user (Users): The user who is following.
        following_user (Users): The user being followed.
        created_at (datetime): The timestamp when the follow occurred.
    """
    user = models.ForeignKey(Users, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(Users, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'following_user')  # Prevent duplicate follows

    def __str__(self):
        return f"{self.user.user_name} follows {self.following_user.user_name}"
