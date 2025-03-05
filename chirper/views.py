from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ChirpForm
from django.utils import timezone
from django.http import HttpRequest, JsonResponse
from .models import Chirps
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
            # Save form (user input) without committing to database yet
            chirp = form.save(commit=False)
            chirp.user_id = request.user
            # Get user ID
            # !!! (after authentication is finished and request.user contains the logged-in user's information)
            # chirp.user_id = Users.objects.get(id=request.user.id)
            chirp.created_time = timezone.now()
            # Default for parent ID is None
            chirp.parent_chirp_id = None  # Set this appropriately if it's a reply
            # Save to database
            chirp.save()
            return redirect("success")

    # Create blank form if a GET (or any other method)
    else:
        form = ChirpForm()

    return render(request, "chirper/chirp_form.html", {"form": form})


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
