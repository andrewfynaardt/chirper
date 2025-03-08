from django.urls import path
from .views import chirp_view, home, profile, like_chirp, still_dev, like_reply, replies_page, reply_to_chirp
from django.views.generic import TemplateView

urlpatterns = [
    # Home page template
    path("home/", home, name="home"),  # Added home URL
    
    # Profile page
    path("profile/", profile, name="profile"),
    
    # Success page after user uploaded their chirp
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),  # Fixed template path
    
    # Still in development page
    path("null/", still_dev, name="still_dev"),
    
    # Like/Unlike a chirp
    path("like/<int:chirp_id>/", like_chirp, name="like_chirp"),
    
    # Create a new chirp
    path('create/', chirp_view, name='chirp_view'),  # Using 'chirp_view' to match the original name

    path("chirper/reply/like/<int:reply_id>/", like_reply, name="like_reply"),

    path("chirper/<int:chirp_id>/replies/", replies_page, name="replies_page"),

    path("chirper/reply/<int:chirp_id>/", reply_to_chirp, name="reply_to_chirp"),

]
