from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count

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
    likes = models.ManyToManyField(User, related_name="liked_chirps", blank=True)

    # Field for replies
    parent_chirp = models.ForeignKey(
        'self',  # Self-referential ForeignKey
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="child_replies"
    )

    # Method that returns the total number of likes
    def total_likes(self):
        return self.likes.count()
    
    # Function that returns the total number of replies
    def total_replies(self):
        """
        Returns the total number of replies to this chirp.
        """
        return self.replies.count()
    
    # Function that returns the most recent reply
    def most_recent_reply(self):
        """
        Returns the timestamp of the most recent reply or the chirp's creation time if no replies exist.
        """
        if self.replies.count() > 0:
            return self.replies.latest('created_time').created_time
        return self.created_time

    def __str__(self):
        return self.chirp_body[:20]
    
    @classmethod
    def get_filtered_chirps(cls, request, filter_type, sort_type):
        """Returns a queryset of chirps based on the filter and sort parameters."""
        match filter_type:
            case "following":
                filtered_chirps = cls.objects.filter(user_id__in=request.user.following.all())
            case "own":
                filtered_chirps = cls.objects.filter(user_id=request.user)
            case "all":
                filtered_chirps = cls.objects.all()
            case default:
                filtered_chirps = cls.objects.all()
        
        match sort_type:
            case "most_likes":
                filtered_chirps = filtered_chirps.annotate(likes_count=Count('likes'))
                filtered_chirps = filtered_chirps.order_by('-likes_count')
            # TODO: Implement sorting by most replies and latest reply when replies are working
            # case "most_replies":
            #     filtered_chirps = filtered_chirps.annotate(replies_count=Count('replies'))
            #     filtered_chirps = filtered_chirps.order_by('-replies_count')
            # case "latest_reply":
            #     filtered_chirps = filtered_chirps.order_by(cls.replies.order_by('-created_time')[0])
            case "date":
                filtered_chirps = filtered_chirps.order_by("-created_time")
            case default:
                filtered_chirps = filtered_chirps.order_by("-created_time")

        return filtered_chirps
    

# Create your models here.
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

    likes = models.ManyToManyField(User, related_name="liked_reply_chirps", blank=True)

    # Function that returns the total number of likes
    def total_reply_likes(self):
        """
        Returns the total number of likes for this reply.
        """
        return self.likes.count()

    def __str__(self):
        return f"Reply by {self.user.username} to Chirp {self.chirp.id}"
