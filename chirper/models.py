# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
        User, on_delete=models.SET_NULL, null=True, related_name="chirps"
    )
    created_time = models.DateTimeField(default=timezone.now)
    parent_chirp_id = models.ForeignKey(
        "self",  # Another chirp's ID
        on_delete=models.SET_NULL,
        null=True,
    )
    likes = models.ManyToManyField(User, related_name="liked_chirps", blank=True)

    # Function that returns the total number of likes
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user_id.username if self.user_id else 'Unknown'}: {self.chirp_body[:20]}"
