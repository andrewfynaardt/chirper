from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ChirpForm
from .models import Chirp, Reply, UserFollowing

# Profile view
def profile(request):
    return render(request, "profile.html")

# Home view
def home(request):
    chirps = Chirp.objects.all().order_by("-created_time")  # Fetch chirps
    form = ChirpForm()
    return render(request, "home.html", {"chirps": chirps, "form": form})

# Chirp submission view
@login_required
def chirp_view(request):
    """
    The view to display the chirpForm to users.
    """
    if request.method == "POST":
        form = ChirpForm(request.POST)

        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user = request.user  # Ensure chirp is linked to user
            chirp.created_time = timezone.now()
            chirp.parent_chirp_id = None  # Update if replying to a chirp
            chirp.save()
            return redirect("home")  # Ensure 'home' exists in urls.py

    else:
        form = ChirpForm()

    return render(request, "chirper/chirp_form.html", {"form": form})

# Reply to a chirp
@login_required
def reply_to_chirp(request, chirp_id):
    """
    Allows users to reply to a chirp.
    """
    chirp = get_object_or_404(Chirp, id=chirp_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Reply.objects.create(user=request.user, chirp=chirp, content=content)
    return redirect("chirp_detail", chirp_id=chirp.id)  # Ensure 'chirp_detail' exists in urls.py

# Follow a user
@login_required
def follow_user(request, user_id):
    """
    Allows users to follow another user.
    """
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow:
        UserFollowing.objects.get_or_create(user=request.user, following_user=user_to_follow)
    return redirect("profile_view", username=user_to_follow.username)  # Ensure 'profile_view' exists

# Unfollow a user
@login_required
def unfollow_user(request, user_id):
    """
    Allows users to unfollow another user.
    """
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollowing.objects.filter(user=request.user, following_user=user_to_unfollow).delete()
    return redirect("profile_view", username=user_to_unfollow.username)  # Ensure 'profile_view' exists

# Display user profile
def profile_view(request, username):
    """
    Displays the profile page of a user, showing their chirps and follow stats.
    """
    profile_user = get_object_or_404(User, username=username)
    chirps = Chirp.objects.filter(user=profile_user).order_by("-created_time")  # Use 'created_time'
    
    followers_count = UserFollowing.objects.filter(following_user=profile_user).count()
    following_count = UserFollowing.objects.filter(user=profile_user).count()

    is_following = (
        request.user.is_authenticated
        and UserFollowing.objects.filter(user=request.user, following_user=profile_user).exists()
    )

    return render(
        request,
        "profile.html",
        {
            "profile_user": profile_user,
            "chirps": chirps,
            "followers_count": followers_count,
            "following_count": following_count,
            "is_following": is_following,
        }
    )
