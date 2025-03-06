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


def replies_page(request, chirp_id):
    """
    Replies page for chirps
    """
    chirp = get_object_or_404(Chirps, id=chirp_id)
    return render(request, "replies.html", {"chirp": chirp})


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
        "replies_page", chirp_id=chirp.id
    )  # Ensure 'chirp_detail' exists in urls.py


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
