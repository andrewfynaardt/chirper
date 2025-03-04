"""
chirper/views.py
Updated: 2025-03-03

Django views are created here.
"""



from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ChirpForm
from .models import Chirps, Reply, UserFollowing

# Create your views here.

def profile(request):
    return render(request, 'profile.html')

def home(request):
    chirps = Chirps.objects.all()
    form = ChirpForm()
    return render(request, 'chirper/home.html', {'chirps': chirps, 'form': form})

# Existing chirpForm view
def chirpForm_view(request):
    """
    The view to display the chirpForm to users to create their chirp.
    """
    
    if request.method == 'POST':
        form = ChirpForm(request.POST)
        
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.created_time = timezone.now()
            chirp.parent_chirp_id = None  # Update if replying to a chirp
            chirp.save()
            return redirect('home')

    else:
        form = ChirpForm()

    return render(request, 'chirper/home.html')

def chirp_view(request):
    """
    The view to show chirps from the database to the user.
    """
    chirps = Chirps.objects.all()
    return render(request, "chirper/chirp_fragment.html", {"chirps": chirps})

# New Views for Replies and Following Users

@login_required
def reply_to_chirp(request, chirp_id):
    """
    Allows users to reply to a chirp.
    """
    chirp = get_object_or_404(Chirps, id=chirp_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Reply.objects.create(user=request.user, chirp=chirp, content=content)
    return redirect("chirp_detail", chirp_id=chirp.id)  # Ensure chirp_detail is defined in urls.py


@login_required
def follow_user(request, user_id):
    """
    Allows users to follow another user.
    """
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow:
        UserFollowing.objects.get_or_create(user=request.user, following_user=user_to_follow)
    return redirect("profile", username=user_to_follow.username)  # Ensure profile URL is correct


@login_required
def unfollow_user(request, user_id):
    """
    Allows users to unfollow another user.
    """
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollowing.objects.filter(user=request.user, following_user=user_to_unfollow).delete()
    return redirect("profile", username=user_to_unfollow.username)  # Ensure profile URL is correct


def profile_view(request, username):
    """
    Displays the profile page of a user, showing their chirps and follow stats.
    """
    profile_user = get_object_or_404(User, username=username)
    chirps = Chirps.objects.filter(user=profile_user).order_by('-created_at')
    followers_count = profile_user.followers.count()
    following_count = profile_user.following.count()
    is_following = request.user.is_authenticated and UserFollowing.objects.filter(user=request.user, following_user=profile_user).exists()
    
    return render(request, "profile.html", {
        "profile_user": profile_user,
        "chirps": chirps,
        "followers_count": followers_count,
        "following_count": following_count,
        "is_following": is_following,
    })
