from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ChirpForm
from django.utils import timezone
from django.http import HttpRequest, JsonResponse
from .models import Chirps, Reply, UserFollowing, User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile(request):
    return render(request, "profile.html")


def still_dev(request):
    return render(request, "still_dev.html")


def chirp_view(request: HttpRequest):
    """
    The view to display the chirpForm to users.
    """

    # Process the form data if it's a POST request
    if request.method == "POST":
        # Create a form instance and fill in data gained from the request
        form = ChirpForm(request.POST)

        # Save and redirect to success page if from is valid
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user_id = request.user
            # Get user ID
            # !!! (after authentication is finished and request.user contains the logged-in user's information)
            # chirp.user_id = Users.objects.get(id=request.user.id)
            chirp.created_time = timezone.now()
            chirp.parent_chirp_id = None  # Update if replying to a chirp
            chirp.save()
            return redirect("success")

    else:
        form = ChirpForm()

    return render(request, "chirper/chirp_form.html", {"form": form})


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
    return redirect(
        "chirp_detail", chirp_id=chirp.id
    )  # Ensure 'chirp_detail' exists in urls.py


@login_required
def follow_user(request, user_id):
    """
    Allows users to follow another user.
    """
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow:
        UserFollowing.objects.get_or_create(
            user=request.user, following_user=user_to_follow
        )
    return redirect(
        "profile", username=user_to_follow.username
    )  # Ensure profile URL is correct


@login_required
def unfollow_user(request, user_id):
    """
    Allows users to unfollow another user.
    """
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollowing.objects.filter(
        user=request.user, following_user=user_to_unfollow
    ).delete()
    return redirect(
        "profile", username=user_to_unfollow.username
    )  # Ensure profile URL is correct


def profile_view(request, username):
    """
    Displays the profile page of a user, showing their chirps and follow stats.
    """
    profile_user = get_object_or_404(User, username=username)
    chirps = Chirps.objects.filter(user=profile_user).order_by("-created_at")
    followers_count = profile_user.followers.count()
    following_count = profile_user.following.count()
    is_following = (
        request.user.is_authenticated
        and UserFollowing.objects.filter(
            user=request.user, following_user=profile_user
        ).exists()
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
        },
    )


def home(request):
    form = ChirpForm()  # Empty form to pass to Modal
    chirps = Chirps.objects.all().order_by("-created_time")  # Gets current chirps
    return render(
        request, "home.html", {"chirps": chirps, "form": form}
    )  # Passes chirps to home template


@login_required
def like_chirp(request, chirp_id):
    """Lke/Unlike Chirps"""
    chirp = get_object_or_404(Chirps, id=chirp_id)

    if request.user in chirp.likes.all():
        chirp.likes.remove(request.user)  # Unlike
        liked = False
    else:
        chirp.likes.add(request.user)  # Like
        liked = True

    return JsonResponse(chirp.total_likes())
