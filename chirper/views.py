from django.shortcuts import render, redirect
from .forms import ChirpForm
from django.utils import timezone


# Create your views here.
def profile(request):
    return render(request, "profile.html")


def chirp_view(request):
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
    return render(request, "home.html")
