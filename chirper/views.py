from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from .forms import ChirpForm
from .models import Chirps, Reply, UserFollowing, User

# Profile view
def profile(request):
    return render(request, "profile.html")

# place holder to let user know page is still in development
def still_dev(request):
    return render(request, "still_dev.html")

# Home view
def home(request):
    # Filter chirps based on user selection
    print(request.COOKIES)
    sort_type = request.COOKIES.get("sort_type", "date")
    chirps = Chirps.get_filtered_chirps(request, "all", sort_type)
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
            chirp.user_id = request.user  # Ensure chirp is linked to user
            chirp.created_time = timezone.now()
            chirp.parent_chirp_id = None  # Update if replying to a chirp
            chirp.save()
            return redirect("success")

    else:
        form = ChirpForm()

    return render(request, "chirper/chirp_form.html", {"form": form})

# Reply to chirp
@login_required
def reply_to_chirp(request, chirp_id):
    """
    Allows users to reply to a chirp.
    """
    parent_chirp = get_object_or_404(Chirps, id=chirp_id)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            # Create a new chirp as a reply
            Chirps.objects.create(
                chirp_body=content,
                user_id=request.user,
                created_time=timezone.now(),
                parent_chirp=parent_chirp  # Link the reply to the parent chirp
            )
            return redirect("home")  # Redirect after replying
    
    return render(request, "reply_form.html", {"parent_chirp": parent_chirp})


# # Follow a user
# @login_required
# def follow_user(request, user_id):
#     """
#     Allows users to follow another user.
#     """
#     user_to_follow = get_object_or_404(User, id=user_id)
#     if request.user != user_to_follow:
#         UserFollowing.objects.get_or_create(user=request.user, following_user=user_to_follow)
#     return redirect("profile_view", username=user_to_follow.username)  # Ensure 'profile_view' exists

# # Unfollow a user
# @login_required
# def unfollow_user(request, user_id):
#     """
#     Allows users to unfollow another user.
#     """
#     user_to_unfollow = get_object_or_404(User, id=user_id)
#     UserFollowing.objects.filter(user=request.user, following_user=user_to_unfollow).delete()
#     return redirect("profile_view", username=user_to_unfollow.username)  # Ensure 'profile_view' exists

# Display user profile
def profile_view(request, username):
    """
    Displays the profile page of a user, showing their chirps and follow stats.
    """
    profile_user = get_object_or_404(User, username=username)
    chirps = Chirps.objects.filter(user=profile_user).order_by("-created_time")  # Use 'created_time'
    
    # followers_count = UserFollowing.objects.filter(following_user=profile_user).count()
    # following_count = UserFollowing.objects.filter(user=profile_user).count()

    # is_following = (
    #     request.user.is_authenticated
    #     and UserFollowing.objects.filter(user=request.user, following_user=profile_user).exists()
    # )

    return render(
        request,
        "profile.html",
        {
            "profile_user": profile_user,
            "chirps": chirps,
            # "followers_count": followers_count,
            # "following_count": following_count,
            # "is_following": is_following,
        }
    )


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
