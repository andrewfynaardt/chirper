from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from .forms import ChirpForm
from .models import Chirp, Reply, User

# Profile view
def profile(request):
    """
    Render the user's profile page.
    """
    return render(request, "profile.html")

# place holder to let user know page is still in development
def still_dev(request):
    """
    Render a placeholder page for features still in development.
    """
    return render(request, "still_dev.html")

# Home view
def home(request):
    """
    Render the home page with a list of chirps, filter chirps based on user selection.
    """
    print(request.COOKIES)
    sort_type = request.COOKIES.get("sort_type", "date")
    chirps = Chirp.get_filtered_chirps(request, "all", sort_type)
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
            return redirect("success")

    else:
        form = ChirpForm()

    return render(request, "chirper/chirp_form.html", {"form": form})

def replies_page(request, chirp_id):
    """
    Replies page for chirps.
    """
    chirp = get_object_or_404(Chirp, id=chirp_id)
    return render(request, "replies.html", {"chirp": chirp})

@login_required
def reply_to_chirp(request, chirp_id):
    """
    Allows users to reply to a chirp.
    """
    parent_chirp = get_object_or_404(Chirp, id=chirp_id)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Reply.objects.create(user=request.user, chirp=parent_chirp, content=content)

    return redirect("replies_page", chirp_id=parent_chirp.id)
    
# Display user profile
def profile_view(request, username):
    """
    Displays the profile page of a user, showing their chirps and follow stats.
    """
    profile_user = get_object_or_404(User, username=username)
    chirps = Chirp.objects.filter(user=profile_user).order_by("-created_time")  # Use 'created_time'

    return render(
        request,
        "profile.html",
        {
            "profile_user": profile_user,
            "chirps": chirps,
        }
    )


@login_required
def like_chirp(request, chirp_id):
    """Lke/Unlike Chirps"""
    chirp = get_object_or_404(Chirp, id=chirp_id)

    if request.user in chirp.likes.all():
        chirp.likes.remove(request.user)  # Unlike
        liked = False
    else:
        chirp.likes.add(request.user)  # Like
        liked = True

    return JsonResponse(chirp.total_likes())

@login_required
def like_reply(request, reply_id):
    """
    Allows users to like/unlike a reply.
    """
    reply = get_object_or_404(Reply, id=reply_id)

    if request.user in reply.likes.all():
        reply.likes.remove(request.user)  # Unlike
        liked = False
    else:
        reply.likes.add(request.user)  # Like
        liked = True

    return JsonResponse(reply.total_reply_likes())
